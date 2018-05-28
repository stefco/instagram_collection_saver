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
