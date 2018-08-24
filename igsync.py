#!/usr/bin/env python3

"""
Pull saved Instagram posts as JSON, save them to a SQLite database, and
download the associated media.
"""

import os
import sqlite3
from collections import namedtuple
from textwrap import dedent

DEFAULT_COLLECTION_DIR = os.path.expanduser(
    os.path.join("~", "Pictures", "InstagramCollections")
)
DEFAULT_DB_PATH = os.path.join(DEFAULT_COLLECTION_DIR, "insta.sqlite")


def dedent_sql(command):
    """Dedent a SQL command string."""
    lines = command.split('\n')
    return dedent('\n'.join([l for l in lines if not set(l).issubset({' '})]))


class InstagramDb(object):
    """A representation of the database where Instagram posts, users, and
    collections are stored."""

    def __init__(self, path=DEFAULT_DB_PATH):
        """``dbpath`` is the path to the SQLite database that should be used.
        """
        self.path = os.path.realpath(path)
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()

    TABLE_COMMANDS = namedtuple(
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
                name                        text    NOT NULL
            );
        """),
        POSTS=dedent_sql("""
            CREATE TABLE IF NOT EXISTS posts (
                pk                          text    PRIMARY KEY,
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
                has_user_saved              integer NOT NULL,
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
                post_pk                     text NOT NULL,
                url                         text NOT NULL,
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
        for command in self.TABLE_COMMANDS:
            self.cursor.execute(command.strip(';'))
        if commit:
            self.connection.commit()
        return self
