# (c) Stefan Countryman 2018
# Command line tools. Source this file for convenience functions.

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

alias igcolsave="$DIR/ig_collection_saver.py"
igls () {
    ls --color=auto "$@" \
        | sed 's|\(^[^.]*\)\..*$|https://www.instagram.com/p/\1 <- &|'
}
