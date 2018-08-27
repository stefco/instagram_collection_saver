#!/usr/bin/env python3
# (c) Stefan Countryman 2018

"""
Pull saved Instagram posts as JSON, save them to a SQLite database, and
download the associated media.
"""

import os
import sqlite3
import json
import logging
import pickle
from netrc import netrc
from collections import namedtuple
from http.cookiejar import CookieJar
from textwrap import dedent
from urllib.parse import urlparse
from instagram_private_api import Client
from instagram_private_api.errors import ClientConnectionError

LOCAL_STORAGE = os.path.join(os.path.expanduser("~"), ".local", "share",
                             "igsync")
COOKIE_JAR = os.path.join(LOCAL_STORAGE, "cookie.jar")
DEFAULT_COLLECTION_DIR = os.path.expanduser(
    os.path.join("~", "Pictures", "InstagramCollections")
)
DEFAULT_DB_PATH = os.path.join(DEFAULT_COLLECTION_DIR, "insta.sqlite")


def dedent_sql(command):
    """Dedent a SQL command string."""
    lines = command.split('\n')
    return dedent('\n'.join([l for l in lines if not set(l).issubset({' '})]))


def get_media_links(media):
    """Extract the highest-quality media URLs (and media dimensions) from the
    ``media`` item in the JSON object returned by the Instagram API.

    Arguments
    =========
    media : `string`, `dict`
        The only object contained in the ``post`` object returned by
        Instagram's posts API. can either be a JSON string or a dictionary (as
        parsed by ``json.loads``).

    Returns
    =======
    links : list
        A list of dictionaries containing the ``height``, ``width``,
        ``media_type``, and ``url`` of each image in this post.
    """
    if not isinstance(media, dict):
        media = json.loads(media)
    if media['media_type'] == 8:
        return [get_media_links(m)[0] for m in media['carousel_media']]
    if media['media_type'] == 1:
        result = media['image_versions2']['candidates'][0]
    elif media['media_type'] == 2:
        result = media['video_versions'][0]
    else:
        raise ValueError("Unrecognized media_type: " +
                         str(media['media_type']))
    result = {k: result[k] for k in ('height', 'width', 'url')}
    result['media_type'] = media['media_type']
    return [result]


class InstagramDb(object):
    """A representation of the database where Instagram posts, users, and
    collections are stored as well as an interface to the Instagram private
    API."""

    def __init__(self, path=DEFAULT_DB_PATH, username=None, password=None,
                 netrc_path=os.path.expanduser("~/.netrc")):
        """
        Arguments
        =========
        path : `string`
            the path to the SQLite database that should be used.
        username : `string`, optional
            instagram account username. If not provided, will be read from
            ``netrc`` argument. If not available in a netrc file, user will be
            prompted (if possible) for the username. If no username can be
            found through these means, no connection will be made to the
            Instagram API.
        password : `string`, optional
            instagram account password. If not provided, will be read from
            ``netrc`` argument. If not available in a netrc file, user will be
            prompted (if possible) for the password. If no password can be
            found through these means, no connection will be made to the
            Instagram API.
        netrc_path : `string`, optional
            path to the .netrc file from which the Instagram username and
            password will be parsed (if not explicitly provided through init
            arguments).
        """
        self.username = None  # will get overwritten when/if we log in
        self.path = os.path.realpath(path)
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()
        self.netrc_path = netrc_path
        # if username and password were explicitly provided, initialize a
        # connection to instagram.com immediately. otherwise, this connection
        # will be generated as needed.
        if None not in (username, password):
            self.login(username, password)
        elif {username, password} != {None}:
            raise ValueError("must provide both username and password or "
                             "neither.")

    def login(self, username, password):
        """Try to form a new connection to Instagram using the given username
        and password."""
        # try to load cookies from cookie jar
        client_kwargs = dict()
        if os.path.isfile(COOKIE_JAR):
            cookies = CookieJar()
            with open(COOKIE_JAR, 'rb') as cookiejar:
                cookie_string = cookiejar.read()
            # make sure username in cookies is as expected; otherwise,
            # don't use cookies
            try:
                cookies._cookies = pickle.loads(cookie_string)
                cookie_user = [c.value for c in cookies
                               if c.name == 'ds_user']
                if cookie_user == username:
                    client_kwargs['cookie'] = cookie_string
            except:
                logging.warn("Could not parse cookie file.")
        self.client = Client(username, password, **client_kwargs)
        self.username = username

    @property
    def client(self):
        if not hasattr(self, "_client"):
            # get user info from .netrc
            try:
                creds = netrc(self.netrc_path).authenticators("instagram.com")
                self.login(creds[0], creds[2])
            except:
                raise ValueError("Can't find usable .netrc authentication "
                                 "info in given .netrc: " + self.netrc_path)
        return self._client

    @client.setter
    def client(self, value):
        """Set the value of the client and cache the authentication cookies in
        ~/.local/share/igsync/cookie.jar for later use."""
        if not os.path.isdir(LOCAL_STORAGE):
            os.makedirs(LOCAL_STORAGE)
        self._client = value
        with open(COOKIE_JAR, 'wb') as cookiejar:
            cookiejar.write(self.client.cookie_jar.dump())

    TABLE_DEFINITIONS = namedtuple(
        'namespace',
        (
            'USERS',
            'COLLECTIONS',
            'POSTS',
            'COLLECTION_RELATIONS',
            'POST_URLS',
        ),
    )(
        USERS=dedent_sql("""
            CREATE TABLE IF NOT EXISTS users (
                pk                          text    PRIMARY KEY,
                username                    text    NOT NULL,
                full_name                   text    NOT NULL,
                is_private                  integer NOT NULL,
                profile_pic_url             text    NOT NULL
            );
        """),
        COLLECTIONS=dedent_sql("""
            CREATE TABLE IF NOT EXISTS collections (
                pk                          text    PRIMARY KEY,
                name                        text
            );
        """),
        POSTS=dedent_sql("""
            CREATE TABLE IF NOT EXISTS posts (
                pk                          text    PRIMARY KEY,
                code                        text    NOT NULL,
                taken_at                    integer NOT NULL,
                media_type                  integer NOT NULL,
                comment_likes_enabled       integer NOT NULL,
                comment_threading_enabled   integer NOT NULL,
                has_more_comments           integer NOT NULL,
                user_pk                     integer NOT NULL,
                photo_of_you                integer NOT NULL,
                caption_text                text    NOT NULL,
                post_json                   text    NOT NULL,
                like_count                  integer NOT NULL,
                has_viewer_saved            integer NOT NULL,
                FOREIGN KEY (user_pk) REFERENCES users (pk)
                    ON DELETE CASCADE ON UPDATE NO ACTION
            );
        """),
        COLLECTION_RELATIONS=dedent_sql("""
            CREATE TABLE IF NOT EXISTS collection_relations (
                post_pk                     text NOT NULL,
                collection_pk               text NOT NULL,
                PRIMARY KEY (post_pk, collection_pk),
                FOREIGN KEY (post_pk) REFERENCES posts (pk)
                    ON DELETE CASCADE ON UPDATE NO ACTION,
                FOREIGN KEY (collection_pk) REFERENCES collections (pk)
                    ON DELETE CASCADE ON UPDATE NO ACTION
            );
        """),
        POST_URLS=dedent_sql("""
            CREATE TABLE IF NOT EXISTS post_urls (
                post_pk                     text    NOT NULL,
                url                         text    NOT NULL,
                ind                         integer NOT NULL,
                media_type                  integer NOT NULL,
                height                      integer NOT NULL,
                width                       integer NOT NULL,
                download_path               text,
                PRIMARY KEY (post_pk, url),
                FOREIGN KEY (post_pk) REFERENCES posts (pk)
                    ON DELETE CASCADE ON UPDATE NO ACTION
            );
        """),
    )

    def inittables(self, commit=True):
        """Initialize tables in the instagram database if they don't already
        exist. If ``commit`` is ``True`` (default), commit the changes
        immediately. Returns ``self`` to allow for chained commands."""
        for command in self.TABLE_DEFINITIONS:
            self.cursor.execute(command)
        if commit:
            self.connection.commit()
        return self

    def save_user(self, user, overwrite=True, commit=True):
        """Save an instagram user (either a dict or raw JSON returned from the
        API) to this database. If ``overwrite`` is ``True`` (default), replaces
        existing records with the given value; otherwise, existing records are
        left alone. Returns ``self`` to allow for chained commands."""
        if not isinstance(user, dict):
            user = json.loads(user)
        self.cursor.execute(
            'INSERT OR {} INTO users VALUES (?, ?, ?, ?, ?)'.format(
                'REPLACE' if overwrite else 'IGNORE'
            ),
            (
                str(user['pk']),
                str(user['username']),
                str(user['full_name']),
                int(user['is_private']),
                str(user['profile_pic_url'])
            )
        )
        if commit:
            self.connection.commit()
        return self

    def save_collection(self, collection_pk, name=None, overwrite=True,
                        commit=True):
        """Save an instagram collection to this database. ``collection_pk`` is
        the primary key of the collection as returned by Instagram's API and
        ``name`` is the name of the collection as defined by the user. If
        ``overwrite`` is ``True``, overwrite any existing collection (default).
        Otherwise, only create the entry if the collection is not already
        saved. Returns ``self`` to allow for chained commands."""
        self.cursor.execute(
            'INSERT OR {} INTO collections VALUES (?, {})'.format(
                'REPLACE' if overwrite else 'IGNORE',
                'NULL' if name is None else '?'
            ),
            (collection_pk,) if name is None else (collection_pk, name)
        )
        if commit:
            self.connection.commit()
        return self

    def save_urls(self, post, commit=True):
        """Save an instagram post's media URLs to this database's ``post_urls``
        table. ``post`` can be a JSON string or a dict. Returns ``self`` to
        allow for chained commands."""
        if not isinstance(post, dict):
            post = json.loads(post)
        links = [(
            post['media']['pk'],
            link['url'],
            i,
            link['media_type'],
            link['height'],
            link['width']
        ) for i, link in enumerate(get_media_links(post['media']))]
        self.cursor.executemany(
            'INSERT OR IGNORE INTO post_urls VALUES (?, ?, ?, ?, ?, ?, NULL)',
            links
        )
        if commit:
            self.connection.commit()
        return self

    def save_post(self, post, commit=True):
        """Save an instagram post (as raw JSON returned from the API or as a
        dict parsed from said JSON) to this database. Returns ``self`` to allow
        for chained commands."""
        if not isinstance(post, dict):
            post = json.loads(post)
        media = post['media']
        # make sure the user and collection are in their respective tables
        self.save_user(media['user'], overwrite=False, commit=False)
        for collection_pk in media['saved_collection_ids']:
            self.save_collection(collection_pk, overwrite=False, commit=False)
        self.save_urls(post, commit=False)
        # save the post
        self.cursor.execute(
            'INSERT OR REPLACE INTO posts VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)',
            (
                str(media['pk']),
                str(media['code']),
                int(media['taken_at']),
                int(media['media_type']),
                int(media['comment_likes_enabled']),
                int(media['comment_threading_enabled']),
                int(media['has_more_comments']),
                int(media['user']['pk']),
                int(media['photo_of_you']),
                str(media['caption']['text']),
                str(post),
                int(media['like_count']),
                int(media['has_viewer_saved']),
            )
        )
        # save the collections that this post belongs to
        self.cursor.execute(
            'DELETE FROM collection_relations WHERE post_pk=?',
            (media['pk'],)
        )
        self.cursor.executemany(
            'INSERT INTO collection_relations VALUES (?, ?)',
            [(str(media['pk']), str(k)) for k in media['saved_collection_ids']]
        )
        if commit:
            self.connection.commit()
        return self

    def get_anonymous_collections(self):
        """Return a list of collection IDs whose names need to be set."""
        self.cursor.execute("SELECT pk FROM collections WHERE name IS NULL")
        return [res[0] for res in self.cursor.fetchall()]

    def get_all_collections(self):
        """Return a list of all locally saved collection IDs."""
        self.cursor.execute("SELECT pk FROM collections")
        return [res[0] for res in self.cursor.fetchall()]

    def sync_collection_names(self, collection_pks):
        """Get the latest names for the collections whose primary keys are
        specified in ``collection_pks`` and save them to the local database."""
        for pk in collection_pks:
            name = self.client.collection_feed(pk)['collection_name']
            self.save_collection(pk, name, overwrite=True)

    def get_undownloaded_posts(self):
        """Get a list of all post primary keys in the database that have not
        yet been downloaded to a local path."""
        self.cursor.execute("SELECT DISTINCT posts.pk FROM posts "
                            "JOIN post_urls ON posts.pk = post_urls.post_pk "
                            "WHERE post_urls.download_path IS NULL;")
        return self.cursor.fetchall()

    UrlInfo = namedtuple('UrlInfo', ('post_pk', 'code', 'url', 'index'))

    def get_undownloaded_urls(self):
        """Get a list of all media URL rows in the database that have not yet
        been downloaded to a local path."""
        self.cursor.execute(
            "SELECT posts.pk, posts.code, post_urls.url, post_urls.ind "
            "FROM post_urls JOIN posts ON post_urls.post_pk = posts.pk "
            "WHERE post_urls.download_path IS NULL;"
        )
        return [self.UrlInfo(*row) for row in self.cursor.fetchall()]

    @staticmethod
    def get_media_path(urlinfo):
        """Get the default download path from a UrlInfo object (for when we are
        downloading media)"""
        pk = urlinfo.post_pk
        ext = os.path.basename(urlparse(urlinfo.url).path).split('.')[-1]
        filename = '.'.join([urlinfo.code, str(urlinfo.index), ext])
        return os.path.join(*[pk[-3*i-3:-3*i-1] + pk[-3*i-1]
                              for i in range(len(pk)//3)], filename)
