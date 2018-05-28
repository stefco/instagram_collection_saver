<?php
# (c) Stefan Countryman, 2018

set_time_limit(0);
date_default_timezone_set('UTC');

require __DIR__.'/vendor/autoload.php';
# define $username and $password in auth.php
require __DIR__.'/auth.php';

/////// COMMAND LINE OPTIONS ///////
$debug = json_decode($argv[1]);
$truncatedDebug = json_decode($argv[2]);
$collectionsDir = $argv[3];
$collectionNamesToSync = array_slice($argv, 4);
////////////////////////////////////

$ig = new \InstagramAPI\Instagram($debug, $truncatedDebug);

function debug($msg){
    fwrite(STDERR, $msg."\n");
}

debug("Logging in as $username...");

// A function for getting the instagram URL, taken from:
// https://medium.com/stirtingale/how-to-convert-an-instagram-id-to-a-url-in-php-cbe77ed7aa00
// Also at
// https://gist.github.com/stirtingale/87e44b865343061edc9b09c14571fceb#file-instagram_id_to_url-php
// based on ggwarpig stackoverflow anwser to 
// "Where do I find the Instagram media ID of a image"
// @ https://stackoverflow.com/a/37246231
function instagram_id_to_url($instagram_id){
    $url_prefix = "https://www.instagram.com/p/";
    if(!empty(strpos($instagram_id, '_'))){
        $parts = explode('_', $instagram_id);
        $instagram_id = $parts[0];
        $userid = $parts[1];
    }
    $alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_';
    while($instagram_id > 0){
        $remainder = $instagram_id % 64;
        $instagram_id = ($instagram_id-$remainder) / 64;
        $url_suffix = $alphabet{$remainder} . $url_suffix;
    };
    return $url_prefix.$url_suffix;
}

// URL could be video or photo, in carousel or not
function get_urls($media){
    $id = $media->getId();
    $urlHolder = $media->getVideoVersions();

    if ($urlHolder === null) {
        // maybe means we have an image
        debug("      media has no video version: $id");
        $urlHolder = $media->getImageVersions2();
    } else {
        // this is a video; return its URL
        return [$urlHolder[0]->getUrl()];
    }

    if ($urlHolder === null) {
        // means we have a carousel; handle them independently
        debug("      media has no image version: $id");
        $urls = array();
        $carousel = $media->getCarouselMedia();
        foreach($carousel as $i => $cmedia){
            array_push($urls, get_urls($cmedia)[0]);
        }
        return $urls;
    }
    // It was an image after all
    return [$urlHolder->getCandidates()[0]->getUrl()];
}

try {
    $ig->login($username, $password);
} catch (\Exception $e) {
    echo 'Something went wrong while logging in: '.$e->getMessage()."\n";
    exit(1);
}

try {
    $allCollectionsList = $ig->collection->getList();
    $allCollections = $allCollectionsList->getItems();
    $collectionsToSync = array();

    /////// PICK COLLECTIONS TO SYNC ///////
    if (count($collectionNamesToSync) === 0) {
        debug("Syncing all collections.");
        $collectionsToSync = $allCollections;
    } else {
        debug("Looking for specific collections:");
        foreach($collectionNamesToSync as $i => $name){
            debug("  $name");
        }
        foreach($allCollections as $i => $collection) {
            $name = $collection->getCollectionName();
            if (in_array($name, $collectionNamesToSync, true)) {  # strict=true
                debug("Found collection on Instagram: $name");
                array_push($collectionsToSync, $collection);
            }
        }
    }

    /////// SYNC COLLECTIONS IN ORDER ///////
    debug("Syncing collections now.");
    foreach($collectionsToSync as $i => $collection) {
        $name = $collection->getCollectionName();
        debug("On collection: $name");
        $colDir = $collectionsDir."/".$name;
        debug("  Collection directory: $colDir");
        if (!file_exists($colDir)) {
            debug("  Directory does not exist, making now...");
            mkdir($colDir, 0777, true);  # recursive=true
        }
        $colId = $collection->getCollectionId();
        debug("  Collection ID: $colId");

        // ITERATE THROUGH PAGES OF CONTENT
        $maxId = null;  # On the first page...
        $sleepFirst = false;  # don't sleep on the first loop...
        do {
            if ($sleepFirst) {
                // Sleep for 3-7 seconds before requesting the next page. This
                // is just an example of an okay sleep time. It is very
                // important that your scripts always pause between requests
                // that may run very rapidly, otherwise Instagram will throttle
                // you temporarily for abusing their API!
                debug("    Processed a page, sleeping for 3-7s...");
                sleep(rand(3, 7));
            } else {
                // Don't want to sleep on the first loop but do want to sleep
                // before subsequent loops.
                debug("    Processing first page.");
                $sleepFirst = true;
            }
            $response = $ig->collection->getFeed($colId, $maxId);
            $feedItems = $response->getItems();


            // Save each image
            foreach($feedItems as $j => $item) {
                $media = $item->getMedia();
                $id = $media->getId();
                $username = $media->getUser()->getUsername();
                $post_url = instagram_id_to_url($id);
                $urls = get_urls($media);
                $num_urls = count($urls);
                foreach($urls as $k => $url){
                    $remoteFname = parse_url($url, PHP_URL_PATH);
                    $ext = pathinfo($remoteFname, PATHINFO_EXTENSION);
                    $fname_base = basename(parse_url($post_url, PHP_URL_PATH));
                    if ($num_urls != 1){
                        $kstr = (string) $k;
                        $fname_base = $fname_base."-".$kstr;
                    }
                    $fname = $fname_base.".".$ext;

                    // Save the actual file in the directory holding all
                    // collections if it isn't already there...
                    $filepath = $collectionsDir."/".$fname;
                    if (!file_exists($filepath)) {
                        debug("      File not saved, fetching: $fname");
                        debug("      post url: $post_url");
                        sleep(rand(1, 3));
                        copy($url, $filepath);
                    }

                    // Also symlink that file into the collection we are
                    // updating
                    $linkpath = $colDir."/".$fname;
                    if (!file_exists($linkpath)) {
                        debug("      Symlinking to: $linkpath");
                        symlink($filepath, $linkpath);
                    }
                }
            }

            // Now we must update the maxId variable to the "next page".  This
            // will be a null value again when we've reached the last page!
            // And we will stop looping through pages as soon as maxId becomes
            // null.
            $maxId = $response->getNextMaxId();

        // Must use "!==" for comparison instead of "!=".
        } while ($maxId !== null);
        debug("Finished collection: $name");
    }
    debug("Finished all requested syncing operations.");
} catch (\Exception $e) {
    echo 'Something went wrong: '.$e->getMessage()."\n";
}
