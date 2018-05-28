#!/usr/bin/env python
# (c) Stefan Countryman, 2018

"""
A thin wrapper around saveImages.php. Get images from instagram collections and
save them to an output directory.
"""

import sys
import os
from netrc import netrc
from argparse import ArgumentParser
from numbers import Integral
from collections import namedtuple
from subprocess import Popen, PIPE

DESC = """Download images saved in your Instagram collections and save them to
files on disk. Put authentication info under an "instagram.com" entry in
`.netrc` or enter it at the command line when prompted during script
execution."""
DEFAULT_COLLECTIONS_DIR = os.path.join(os.path.expanduser("~"), "Pictures",
                                       "InstagramCollections")
DEFAULT_COLLECTIONS = ()  # if none are specified, try syncing all
SCRIPTDIR = os.path.realpath(os.path.dirname(__file__))

if __name__ == "__main__":
    PARSER = ArgumentParser(description=DESC)
    ARG = PARSER.add_argument
    ARG("-d", "--collections-dir", default=DEFAULT_COLLECTIONS_DIR, help="""
        The directory that will hold your collections. Photos from each
        collection go into a directory whose name is that of the
        collection.""")
    ARG("-c", "--collections", nargs="*", default=(), help="""
        A list of the collections to sync from Instagram. Use the current name
        of the collection. If no collections are specified (DEFAULT), try to
        sync all collections.""")
    ARG("-v", "--verbose", action="count", default=0, help="""
        Verbosity level, i.e. whether to provide debug output from the
        Instagram PHP client. More `v`s means more verbosity. No `-v` indicates
        no debug info (default); `-v` provides status messages to indicate
        progress; `-vv` provides truncated debug info; and `-vvv` provides full
        debug info.""")
    ARGS = PARSER.parse_args()


# fix python2 input
try:
    input = raw_input  # pylint: disable=redefined-builtin,invalid-name
except NameError:
    pass


def get_auth():
    """Read authentication information from the `.netrc` "instagram.com"
    machine entry. If it isn't stored there, and this is an interactive
    session, prompt the user for that info. If it isn't available anywhere,
    raise an IOError. Returns `username` and `password` as a tuple."""
    import __main__
    interactive = not hasattr(__main__, '__file__')
    username, _account, password = netrc().authenticators("instagram.com")
    if username is None:
        if not interactive:
            raise IOError("Cannot read username from .netrc or user input.")
        username = input("Instagram username:")
    if password is None:
        if not interactive:
            raise IOError("Cannot read password from .netrc or user input.")
        password = input("Password (warning: not hidden):")
    return username, password


def mkdirp(newdir=DEFAULT_COLLECTIONS_DIR):
    """Make directory `newdir` (if it doesn't already exist)."""
    if not os.path.isdir(newdir):
        os.makedirs(newdir)


def verbosity_args(verbosity):
    """Return `debug`, `truncated_debug`, and `logfile` based on verbosity."""
    assert isinstance(verbosity, Integral)
    debug = 'false'
    truncated_debug = 'true'
    logfile = open(os.devnull, 'w')
    if verbosity > 0:
        logfile = sys.stderr
    if verbosity > 1:
        debug = 'true'
    if verbosity > 2:
        truncated_debug = 'false'
    namespace = namedtuple('NameSpace',
                           ('debug', 'truncated_debug', 'logfile'))
    return namespace(debug, truncated_debug, logfile)


def sync(collections=DEFAULT_COLLECTIONS,
         collections_dir=DEFAULT_COLLECTIONS_DIR, debug=False,
         truncated_debug=True, logfile=PIPE, synchronous=False):
    """Try syncing the specified `collections` to the `collections_dir` with
    the specified amount of debug information. Returns the `subprocess.Popen`
    object for the sync process (which is implemented in PHP). If `logfile` is
    provided, prints diagnostic information to that file; otherwise pipes it to
    the returned `Popen` object's `stderr` attribute. Execute syncronously
    (i.e. finish the command before returning) by specifying
    `synchronous=True`."""
    phpfile = os.path.join(SCRIPTDIR, 'saveImages.php')
    username, password = get_auth()
    cmd = [
        'php',
        phpfile,
        str(debug).lower(),
        str(truncated_debug).lower(),
        username,
        password,
        collections_dir,
    ] + list(collections)
    proc = Popen(cmd, stderr=logfile)
    if synchronous:
        proc.wait()
    return proc


def main():
    """Run with the command line options."""
    debug, truncated_debug, logfile = verbosity_args(ARGS.verbose)
    proc = sync(
        collections=ARGS.collections,
        collections_dir=ARGS.collections_dir,
        debug=debug,
        truncated_debug=truncated_debug,
        logfile=logfile,
        synchronous=True
    )
    return proc.returncode


if __name__ == "__main__":
    exit(main())
