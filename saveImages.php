<?php

set_time_limit(0);
date_default_timezone_set('UTC');

require __DIR__.'/vendor/autoload.php';
# define $username and $password in auth.php
require __DIR__.'/auth.php';

/////// CONFIG ///////
$debug = json_decode(argv[1]);
$truncatedDebug = json_decode(argv[2]);
//////////////////////

$ig = new \InstagramAPI\Instagram($debug, $truncatedDebug);

print("Logging in as $username...");

try {
    $ig->login($username, $password);
} catch (\Exception $e) {
    echo 'Something went wrong: '.$e->getMessage()."\n";
    exit(0);
}
