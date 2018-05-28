# Instagram Collection Image Saver

## Installation

Uses [this instagram API](https://github.com/mgp25/Instagram-API/) written in
PHP. Install as follows:

### Composer

Use [Composer](https://getcomposer.org/download/) to install dependencies.
Install it with:

```bash
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
php -r "if (hash_file('SHA384', 'composer-setup.php') === '544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"
php composer-setup.php
php -r "unlink('composer-setup.php');"
```

### Install Instagram PHP

```bash
composer require mgp25/instagram-php
```

## Use

### Authentication

The python-based command line interface to this program will check your
`~/.netrc` file for an "instagram.com" machine entry like the following:

```
machine instagram.com
login your.username
password your.password
```

If such an entry doesn't exist (or if either or both of the login/password
entries are not specified for "instagram.com"), you will be prompted for the
missing login information when the script is called.

### Command Line Interface

Use the `ig_collection_saver.py` script from the command line to download stuff. It's got
a nicer interface than the PHP script (since I'm more familiar with python and
love `argparse` for writing CLIs). See it's capabilities with
`ig_collection_saver.py -h`.

Note that this script is deliberately highly throttled in order to avoid
pissing off Instagram. The intended use is to archive things you've saved, so
it shouldn't *have* to be that fast anyway. It will conservatively wait a
couple of seconds (the actual values are random) between image downloads in
order to avoid taxing Instagram's API more than a normal user would.

#### Examples

Download all of your collections to `~/Pictures/InstagramCollections` with:

```bash
ig_collection_saver.py
```

Download them with verbose progress info (but no hardcore debugging stuff)
using:

```bash
ig_collection_saver.py -v
```

Download only your collection called "Cars" and "Tasty Fruits" (if they exits)
using:

```bash
ig_collection_saver.py -c Cars "Tasty Fruits"
```

### Python Module

You can also use `ig_collection_saver` as a python module (provided you have
added it to `sys.path`). The functionality is pretty limited, but it might be
handy if you like automating things with python.
