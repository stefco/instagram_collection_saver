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

# TODO delet this
var_dump($argv);
var_dump($debug);
var_dump($truncatedDebug);
var_dump($collectionsDir);
var_dump($collectionNamesToSync);

$ig = new \InstagramAPI\Instagram($debug, $truncatedDebug);

fwrite(STDERR, "Logging in as $username...\n");

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
    $urlHolder = $media->getImageVersions2();
    if ($urlHolder === null) {
        // maybe means we have a video
        fwrite(STDERR, "media has no image version: $id\n");
        $urlHolder = $media->getVideoVersions();
    }
    if ($urlHolder === null) {
        // means we have a carousel; handle them independently
        fwrite(STDERR, "media has no video version: $id\n");
        $urls = array();
        $carousel = $media->getCarouselMedia();
        foreach($carousel as $i => $cmedia){
            array_push($urls, get_urls($cmedia)[0]);
        }
        return $urls;
    }
    return [$urlHolder->getCandidates()[0]->getUrl()];
}

try {
    $ig->login($username, $password);
} catch (\Exception $e) {
    echo 'Something went wrong: '.$e->getMessage()."\n";
    exit(0);
}

try {
    $allCollectionsList = $ig->collection->getList();
    $allCollections = $allCollectionsList->getItems();
    $collectionsToSync = array();

    /////// PICK COLLECTIONS TO SYNC ///////
    if (count($collectionNamesToSync) === 0) {
        fwrite(STDERR, "Syncing all collections.\n");
        $collectionsToSync = $allCollections;
    } else {
        fwrite(STDERR, "Looking through more than zero collections.\n");
        foreach($allCollections as $i => $collection) {
            $name = $collection->getCollectionName();
            if (in_array($name, $collectionNamesToSync, true)) {  # strict=true
                fwrite(STDERR, "Found collection on Instagram: $name\n");
                array_push($collectionsToSync, $collection);
            }
        }
    }
    ////////////////////////////////////////

    /////// SYNC COLLECTIONS IN ORDER ///////
    fwrite(STDERR, "Syncing collections now.\n");
    foreach($collectionsToSync as $i => $collection) {
        $name = $collection->getCollectionName();
        fwrite(STDERR, "On collection: $name\n");
        $colDir = $collectionsDir."/".$name;
        fwrite(STDERR, "  Collection directory: $colDir\n");
        if (!file_exists($colDir)) {
            fwrite(STDERR, "  Directory does not exist, making now...\n");
            mkdir($colDir, 0777, true);  # recursive=true
        }
        $colId = $collection->getCollectionId();
        fwrite(STDERR, "  Collection ID: $colId\n");

        // ITERATE THROUGH PAGES OF CONTENT
        $maxId = null;  # On the first page...
        $sleepFirst = false;  # don't sleep on the first loop...
        do {
            if ($sleepFirst) {
                // Sleep for 5 seconds before requesting the next page. This is
                // just an example of an okay sleep time. It is very important that
                // your scripts always pause between requests that may run very
                // rapidly, otherwise Instagram will throttle you temporarily for
                // abusing their API!
                fwrite(STDERR, "    Processed a page, sleeping for 3-7s...\n");
                sleep(rand(3, 7));
            } else {
                // Don't want to sleep on the first loop but do want to sleep
                // before subsequent loops.
                fwrite(STDERR, "    Processing first page.\n");
                $sleepFirst = true;
            }
            $response = $ig->collection->getFeed($colId, $maxId);
            $feedItems = $response->getItems();


            // Let's look at the available methods for this item as well as its
            // JSON contents.
            /* $feedItems[0]->printJson(); // Shows its actual JSON contents (available data). */
            /* $feedItems[0]->printPropertyDescriptions(); // List of supported properties. */
            /* $feedItems[0]->getMedia()->printPropertyDescriptions(); // List of supported properties. */

            // Save each image
            foreach($feedItems as $j => $item) {
                $media = $item->getMedia();
                $id = $media->getId();
                $username = $media->getUser()->getUsername();
                $post_url = instagram_id_to_url($id);
                $urls = get_urls($media);
                $num_urls = count($urls);
                foreach($urls as $k => $url){
                    /* $isReelMedia = $media->getIsReelMedia(); */
                    /* echo "is reel media: $isReelMedia\n"; */
                    /* $videoVersions = $media->getVideoVersions(); */
                    /* $hasVideoVersions = $media->hasVideoVersions(); */
                    /* if ($hasVideoVersions) { */
                        /* $videoVersions->printPropertyDescriptions(); */
                    /* } else { */
                        /* echo "no video versions.\n"; */
                    /* } */
                    /* echo "video versions: $videoVersions\n"; */
                    /* $postUrl = $media->getUrl(); */
                    /* echo "post url: $postUrl\n"; */
                    $remoteFname = parse_url($url, PHP_URL_PATH);
                    $ext = pathinfo($remoteFname, PATHINFO_EXTENSION);
                    /* $fname = urlencode($username."-".$id.".".$ext); */
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
                        fwrite(STDERR, "File not saved, fetching: $fname\n");
                        fwrite(STDERR, "post url: $post_url\n");
                        sleep(rand(0.5, 2));
                        copy($url, $filepath);
                    }

                    // Also symlink that file into the collection we are updating
                    $linkpath = $colDir."/".$fname;
                    if (!file_exists($linkpath)) {
                        fwrite(STDERR, "Symlinking to: $linkpath\n");
                        symlink($filepath, $linkpath);
                    }
                }
            }

            /* $firstItemMedia = $feedItems[0]->getMedia(); */
            /* $firstUrl = $feedItems[0]->getMedia()->getImageVersions2()->getCandidates()[0]->getUrl(); */
            /* fwrite(STDERR, "    First item URL: $firstUrl"); */

            // Now we must update the maxId variable to the "next page".  This
            // will be a null value again when we've reached the last page!
            // And we will stop looping through pages as soon as maxId becomes
            // null.
            $maxId = $response->getNextMaxId();

        // Must use "!==" for comparison instead of "!=".
        } while ($maxId === null);  # TODO delete this line to loop >once.
        /* } while ($maxId !== null); */
    }
    /////////////////////////////////////////
} catch (\Exception $e) {
    echo 'Something went wrong: '.$e->getMessage()."\n";
}
