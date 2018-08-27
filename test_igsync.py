#!/usr/bin/env python3
# (c) Stefan Countryman 2018

"""
Tests for igsync
"""

import sys
import os
from tempfile import NamedTemporaryFile
import igsync

# example JSON
TMP = NamedTemporaryFile(delete=False, suffix='.sqlite')
TMP.file.close()
sys.stderr.write("Writing test database to tempfile: {}".format(TMP.name))
DB = igsync.InstagramDb(path=TMP.name)
CAROUSEL_JSON = r"""{
    "media": {
        "taken_at": "1499717881",
        "pk": "1556068827723262974",
        "id": "1556068827723262974_2261848765",
        "device_timestamp": "13038792543223",
        "media_type": 8,
        "code": "BWYRFq6gOv-",
        "client_cache_key": "MTU1NjA2ODgyNzcyMzI2Mjk3NA==.2",
        "filter_type": 0,
        "comment_likes_enabled": true,
        "comment_threading_enabled": true,
        "has_more_comments": true,
        "next_max_id": "17876646685096381",
        "max_num_visible_preview_comments": 2,
        "preview_comments": [
            {
                "pk": "17875348582126587",
                "user_id": "35763349",
                "text": "Amazing set",
                "type": 0,
                "created_at": "1499794297",
                "created_at_utc": "1499794297",
                "content_type": "comment",
                "status": "Active",
                "bit_flags": 0,
                "user": {
                    "pk": "35763349",
                    "username": "chillg0d",
                    "full_name": "Robb.jpg",
                    "is_private": false,
                    "is_verified": false,
                    "profile_pic_url": "https://scontent-iad3-1.cdninstagram.com/vp/2b6bb99c34396d1842229385e3c6b3aa/5BF8A92D/t51.2885-19/s150x150/36823092_293645828041579_4325600789461467136_n.jpg",
                    "profile_pic_id": "1827350857169293937_35763349"
                },
                "did_report_as_spam": false,
                "media_id": "1556068827723262974"
            },
            {
                "pk": "17876646685096381",
                "user_id": "51613158",
                "text": "Where are the body suits from please",
                "type": 0,
                "created_at": "1499807676",
                "created_at_utc": "1499807676",
                "content_type": "comment",
                "status": "Active",
                "bit_flags": 0,
                "user": {
                    "pk": "51613158",
                    "username": "ericajademurdock",
                    "full_name": "ericajademurdock",
                    "is_private": false,
                    "is_verified": false,
                    "profile_pic_url": "https://scontent-iad3-1.cdninstagram.com/vp/70b4e1accf51282890720f297283a9e5/5C05D5B1/t51.2885-19/s150x150/31279516_217250035717348_1435892521505914880_n.jpg",
                    "profile_pic_id": "1776136202036857888_51613158"
                },
                "did_report_as_spam": false,
                "media_id": "1556068827723262974"
            }
        ],
        "can_view_more_preview_comments": true,
        "comment_count": 15,
        "inline_composer_display_condition": "impression_trigger",
        "carousel_media": [
            {
                "id": "1556068778977213340_2261848765",
                "media_type": 1,
                "image_versions2": {
                    "candidates": [
                        {
                            "width": 1080,
                            "height": 1080,
                            "url": "https://scontent-iad3-1.cdninstagram.com/vp/4012ba7c31408995753a3da47ac95955/5BF88474/t51.2885-15/e35/24331880_194776984414165_2388786859288297472_n.jpg?se=7&ig_cache_key=MTU1NjA2ODc3ODk3NzIxMzM0MA%3D%3D.2"
                        },
                        {
                            "width": 240,
                            "height": 240,
                            "url": "https://scontent-iad3-1.cdninstagram.com/vp/3f89b617b5aeb4df3660e2a7e6760d20/5C3ACE7C/t51.2885-15/e35/s240x240/24331880_194776984414165_2388786859288297472_n.jpg?ig_cache_key=MTU1NjA2ODc3ODk3NzIxMzM0MA%3D%3D.2"
                        }
                    ]
                },
                "original_width": 1080,
                "original_height": 1080,
                "pk": "1556068778977213340",
                "carousel_parent_id": "1556068827723262974_2261848765",
                "usertags": {
                    "in": [
                        {
                            "user": {
                                "pk": "30978460",
                                "username": "jtuliniemi",
                                "full_name": "J. Tuliniemi",
                                "is_private": false,
                                "is_verified": false,
                                "profile_pic_url": "https://scontent-iad3-1.cdninstagram.com/vp/e7f8ec77099c0ec94121942928147ca2/5C058092/t51.2885-19/s150x150/15403531_1355211254499134_5786638901376450560_a.jpg",
                                "profile_pic_id": "1416978428045228714_30978460"
                            },
                            "position": [
                                0.19645731460645,
                                0.135265700483091
                            ],
                            "start_time_in_video_in_sec": null,
                            "duration_in_video_in_sec": null
                        },
                        {
                            "user": {
                                "pk": "977097183",
                                "username": "gwenreecemakeupartist",
                                "full_name": "Gwen Reece",
                                "is_private": false,
                                "is_verified": false,
                                "profile_pic_url": "https://scontent-iad3-1.cdninstagram.com/vp/d6745db8761e92e15c34d44ad51acd82/5C1BFC12/t51.2885-19/s150x150/26872607_186292068784928_8279535729265082368_n.jpg",
                                "profile_pic_id": "1696350945703905357_977097183"
                            },
                            "position": [
                                0.177133643108865,
                                0.349436368343334
                            ],
                            "start_time_in_video_in_sec": null,
                            "duration_in_video_in_sec": null
                        }
                    ]
                }
            },
            {
                "id": "1556068820139912823_2261848765",
                "media_type": 1,
                "image_versions2": {
                    "candidates": [
                        {
                            "width": 1080,
                            "height": 1080,
                            "url": "https://scontent-iad3-1.cdninstagram.com/vp/758a01bf16416909416f4416ae35b3fb/5BFF0471/t51.2885-15/e35/25006159_958047341035782_1218999645175283712_n.jpg?se=7&ig_cache_key=MTU1NjA2ODgyMDEzOTkxMjgyMw%3D%3D.2"
                        },
                        {
                            "width": 240,
                            "height": 240,
                            "url": "https://scontent-iad3-1.cdninstagram.com/vp/1def26257be6e97e07358555c1f83978/5C374679/t51.2885-15/e35/s240x240/25006159_958047341035782_1218999645175283712_n.jpg?ig_cache_key=MTU1NjA2ODgyMDEzOTkxMjgyMw%3D%3D.2"
                        }
                    ]
                },
                "original_width": 1080,
                "original_height": 1080,
                "pk": "1556068820139912823",
                "carousel_parent_id": "1556068827723262974_2261848765",
                "usertags": {
                    "in": [
                        {
                            "user": {
                                "pk": "30978460",
                                "username": "jtuliniemi",
                                "full_name": "J. Tuliniemi",
                                "is_private": false,
                                "is_verified": false,
                                "profile_pic_url": "https://scontent-iad3-1.cdninstagram.com/vp/e7f8ec77099c0ec94121942928147ca2/5C058092/t51.2885-19/s150x150/15403531_1355211254499134_5786638901376450560_a.jpg",
                                "profile_pic_id": "1416978428045228714_30978460"
                            },
                            "position": [
                                0.22222222222222202,
                                0.31803542673107804
                            ],
                            "start_time_in_video_in_sec": null,
                            "duration_in_video_in_sec": null
                        },
                        {
                            "user": {
                                "pk": "977097183",
                                "username": "gwenreecemakeupartist",
                                "full_name": "Gwen Reece",
                                "is_private": false,
                                "is_verified": false,
                                "profile_pic_url": "https://scontent-iad3-1.cdninstagram.com/vp/d6745db8761e92e15c34d44ad51acd82/5C1BFC12/t51.2885-19/s150x150/26872607_186292068784928_8279535729265082368_n.jpg",
                                "profile_pic_id": "1696350945703905357_977097183"
                            },
                            "position": [
                                0.188405797101449,
                                0.12318840579710101
                            ],
                            "start_time_in_video_in_sec": null,
                            "duration_in_video_in_sec": null
                        }
                    ]
                }
            },
            {
                "id": "1556068781686568955_2261848765",
                "media_type": 1,
                "image_versions2": {
                    "candidates": [
                        {
                            "width": 1080,
                            "height": 1080,
                            "url": "https://scontent-iad3-1.cdninstagram.com/vp/090117395dbe3e7c08493b5a34adcb53/5C099D10/t51.2885-15/e35/25012179_140200323354141_3532308626104385536_n.jpg?se=7&ig_cache_key=MTU1NjA2ODc4MTY4NjU2ODk1NQ%3D%3D.2"
                        },
                        {
                            "width": 240,
                            "height": 240,
                            "url": "https://scontent-iad3-1.cdninstagram.com/vp/5f31c1e3113b666a7794604b213a978e/5BFEE418/t51.2885-15/e35/s240x240/25012179_140200323354141_3532308626104385536_n.jpg?ig_cache_key=MTU1NjA2ODc4MTY4NjU2ODk1NQ%3D%3D.2"
                        }
                    ]
                },
                "original_width": 1080,
                "original_height": 1080,
                "pk": "1556068781686568955",
                "carousel_parent_id": "1556068827723262974_2261848765",
                "usertags": {
                    "in": [
                        {
                            "user": {
                                "pk": "30978460",
                                "username": "jtuliniemi",
                                "full_name": "J. Tuliniemi",
                                "is_private": false,
                                "is_verified": false,
                                "profile_pic_url": "https://scontent-iad3-1.cdninstagram.com/vp/e7f8ec77099c0ec94121942928147ca2/5C058092/t51.2885-19/s150x150/15403531_1355211254499134_5786638901376450560_a.jpg",
                                "profile_pic_id": "1416978428045228714_30978460"
                            },
                            "position": [
                                0.30354264853657104,
                                0.66183574879227
                            ],
                            "start_time_in_video_in_sec": null,
                            "duration_in_video_in_sec": null
                        },
                        {
                            "user": {
                                "pk": "359597261",
                                "username": "aisling_tara",
                                "full_name": "Aisling Tara",
                                "is_private": false,
                                "is_verified": false,
                                "profile_pic_url": "https://scontent-iad3-1.cdninstagram.com/vp/98f9b33736b017df63cce70d60c88e82/5BFD93C9/t51.2885-19/s150x150/33545973_260793151146887_3930585281379434496_n.jpg",
                                "profile_pic_id": "1803730515250779444_359597261"
                            },
                            "position": [
                                0.5925925803069331,
                                0.677938783802272
                            ],
                            "start_time_in_video_in_sec": null,
                            "duration_in_video_in_sec": null
                        },
                        {
                            "user": {
                                "pk": "977097183",
                                "username": "gwenreecemakeupartist",
                                "full_name": "Gwen Reece",
                                "is_private": false,
                                "is_verified": false,
                                "profile_pic_url": "https://scontent-iad3-1.cdninstagram.com/vp/d6745db8761e92e15c34d44ad51acd82/5C1BFC12/t51.2885-19/s150x150/26872607_186292068784928_8279535729265082368_n.jpg",
                                "profile_pic_id": "1696350945703905357_977097183"
                            },
                            "position": [
                                0.21417066786024302,
                                0.35024154589371903
                            ],
                            "start_time_in_video_in_sec": null,
                            "duration_in_video_in_sec": null
                        }
                    ]
                }
            },
            {
                "id": "1556068787768320774_2261848765",
                "media_type": 1,
                "image_versions2": {
                    "candidates": [
                        {
                            "width": 1080,
                            "height": 1080,
                            "url": "https://scontent-iad3-1.cdninstagram.com/vp/de0ad4da6d6cfdad7f475ad4b976260f/5C3BAEFB/t51.2885-15/e35/24839072_1890541944594321_3452695613362143232_n.jpg?se=7&ig_cache_key=MTU1NjA2ODc4Nzc2ODMyMDc3NA%3D%3D.2"
                        },
                        {
                            "width": 240,
                            "height": 240,
                            "url": "https://scontent-iad3-1.cdninstagram.com/vp/cfa6fadc3c194b0edf7176100030435d/5C38E9C2/t51.2885-15/e35/s240x240/24839072_1890541944594321_3452695613362143232_n.jpg?ig_cache_key=MTU1NjA2ODc4Nzc2ODMyMDc3NA%3D%3D.2"
                        }
                    ]
                },
                "original_width": 1080,
                "original_height": 1080,
                "pk": "1556068787768320774",
                "carousel_parent_id": "1556068827723262974_2261848765",
                "usertags": {
                    "in": [
                        {
                            "user": {
                                "pk": "30978460",
                                "username": "jtuliniemi",
                                "full_name": "J. Tuliniemi",
                                "is_private": false,
                                "is_verified": false,
                                "profile_pic_url": "https://scontent-iad3-1.cdninstagram.com/vp/e7f8ec77099c0ec94121942928147ca2/5C058092/t51.2885-19/s150x150/15403531_1355211254499134_5786638901376450560_a.jpg",
                                "profile_pic_id": "1416978428045228714_30978460"
                            },
                            "position": [
                                0.590177121369735,
                                0.5684379909349521
                            ],
                            "start_time_in_video_in_sec": null,
                            "duration_in_video_in_sec": null
                        },
                        {
                            "user": {
                                "pk": "359597261",
                                "username": "aisling_tara",
                                "full_name": "Aisling Tara",
                                "is_private": false,
                                "is_verified": false,
                                "profile_pic_url": "https://scontent-iad3-1.cdninstagram.com/vp/98f9b33736b017df63cce70d60c88e82/5BFD93C9/t51.2885-19/s150x150/33545973_260793151146887_3930585281379434496_n.jpg",
                                "profile_pic_id": "1803730515250779444_359597261"
                            },
                            "position": [
                                0.302737507843165,
                                0.424315595396475
                            ],
                            "start_time_in_video_in_sec": null,
                            "duration_in_video_in_sec": null
                        },
                        {
                            "user": {
                                "pk": "977097183",
                                "username": "gwenreecemakeupartist",
                                "full_name": "Gwen Reece",
                                "is_private": false,
                                "is_verified": false,
                                "profile_pic_url": "https://scontent-iad3-1.cdninstagram.com/vp/d6745db8761e92e15c34d44ad51acd82/5C1BFC12/t51.2885-19/s150x150/26872607_186292068784928_8279535729265082368_n.jpg",
                                "profile_pic_id": "1696350945703905357_977097183"
                            },
                            "position": [
                                0.66183574879227,
                                0.31642512077294604
                            ],
                            "start_time_in_video_in_sec": null,
                            "duration_in_video_in_sec": null
                        }
                    ]
                }
            },
            {
                "id": "1556068804444957203_2261848765",
                "media_type": 1,
                "image_versions2": {
                    "candidates": [
                        {
                            "width": 1080,
                            "height": 1080,
                            "url": "https://scontent-iad3-1.cdninstagram.com/vp/2c421648ac910c1457b4f137d6e342f4/5C00A62A/t51.2885-15/e35/24845158_403902786713284_3494112429674070016_n.jpg?se=7&ig_cache_key=MTU1NjA2ODgwNDQ0NDk1NzIwMw%3D%3D.2"
                        },
                        {
                            "width": 240,
                            "height": 240,
                            "url": "https://scontent-iad3-1.cdninstagram.com/vp/3f31c5b1769ac6ad8c494f8e020e6d5e/5C035F22/t51.2885-15/e35/s240x240/24845158_403902786713284_3494112429674070016_n.jpg?ig_cache_key=MTU1NjA2ODgwNDQ0NDk1NzIwMw%3D%3D.2"
                        }
                    ]
                },
                "original_width": 1080,
                "original_height": 1080,
                "pk": "1556068804444957203",
                "carousel_parent_id": "1556068827723262974_2261848765",
                "usertags": {
                    "in": [
                        {
                            "user": {
                                "pk": "30978460",
                                "username": "jtuliniemi",
                                "full_name": "J. Tuliniemi",
                                "is_private": false,
                                "is_verified": false,
                                "profile_pic_url": "https://scontent-iad3-1.cdninstagram.com/vp/e7f8ec77099c0ec94121942928147ca2/5C058092/t51.2885-19/s150x150/15403531_1355211254499134_5786638901376450560_a.jpg",
                                "profile_pic_id": "1416978428045228714_30978460"
                            },
                            "position": [
                                0.22544282185282602,
                                0.34460545046893803
                            ],
                            "start_time_in_video_in_sec": null,
                            "duration_in_video_in_sec": null
                        },
                        {
                            "user": {
                                "pk": "359597261",
                                "username": "aisling_tara",
                                "full_name": "Aisling Tara",
                                "is_private": false,
                                "is_verified": false,
                                "profile_pic_url": "https://scontent-iad3-1.cdninstagram.com/vp/98f9b33736b017df63cce70d60c88e82/5BFD93C9/t51.2885-19/s150x150/33545973_260793151146887_3930585281379434496_n.jpg",
                                "profile_pic_id": "1803730515250779444_359597261"
                            },
                            "position": [
                                0.539452483688575,
                                0.5354267065075861
                            ],
                            "start_time_in_video_in_sec": null,
                            "duration_in_video_in_sec": null
                        },
                        {
                            "user": {
                                "pk": "977097183",
                                "username": "gwenreecemakeupartist",
                                "full_name": "Gwen Reece",
                                "is_private": false,
                                "is_verified": false,
                                "profile_pic_url": "https://scontent-iad3-1.cdninstagram.com/vp/d6745db8761e92e15c34d44ad51acd82/5C1BFC12/t51.2885-19/s150x150/26872607_186292068784928_8279535729265082368_n.jpg",
                                "profile_pic_id": "1696350945703905357_977097183"
                            },
                            "position": [
                                0.24235104669887203,
                                0.087761674718196
                            ],
                            "start_time_in_video_in_sec": null,
                            "duration_in_video_in_sec": null
                        }
                    ]
                }
            },
            {
                "id": "1556068813202776631_2261848765",
                "media_type": 1,
                "image_versions2": {
                    "candidates": [
                        {
                            "width": 1080,
                            "height": 1080,
                            "url": "https://scontent-iad3-1.cdninstagram.com/vp/bce84ad0840a3b1082c4081ba3864fe4/5C19E716/t51.2885-15/e35/25013935_145404159568535_2577928891062550528_n.jpg?se=7&ig_cache_key=MTU1NjA2ODgxMzIwMjc3NjYzMQ%3D%3D.2"
                        },
                        {
                            "width": 240,
                            "height": 240,
                            "url": "https://scontent-iad3-1.cdninstagram.com/vp/d24207e198d28739355e02c242786836/5C06AE1E/t51.2885-15/e35/s240x240/25013935_145404159568535_2577928891062550528_n.jpg?ig_cache_key=MTU1NjA2ODgxMzIwMjc3NjYzMQ%3D%3D.2"
                        }
                    ]
                },
                "original_width": 1080,
                "original_height": 1080,
                "pk": "1556068813202776631",
                "carousel_parent_id": "1556068827723262974_2261848765",
                "usertags": {
                    "in": [
                        {
                            "user": {
                                "pk": "30978460",
                                "username": "jtuliniemi",
                                "full_name": "J. Tuliniemi",
                                "is_private": false,
                                "is_verified": false,
                                "profile_pic_url": "https://scontent-iad3-1.cdninstagram.com/vp/e7f8ec77099c0ec94121942928147ca2/5C058092/t51.2885-19/s150x150/15403531_1355211254499134_5786638901376450560_a.jpg",
                                "profile_pic_id": "1416978428045228714_30978460"
                            },
                            "position": [
                                0.21095006822963802,
                                0.19404185566925203
                            ],
                            "start_time_in_video_in_sec": null,
                            "duration_in_video_in_sec": null
                        },
                        {
                            "user": {
                                "pk": "359597261",
                                "username": "aisling_tara",
                                "full_name": "Aisling Tara",
                                "is_private": false,
                                "is_verified": false,
                                "profile_pic_url": "https://scontent-iad3-1.cdninstagram.com/vp/98f9b33736b017df63cce70d60c88e82/5BFD93C9/t51.2885-19/s150x150/33545973_260793151146887_3930585281379434496_n.jpg",
                                "profile_pic_id": "1803730515250779444_359597261"
                            },
                            "position": [
                                0.521739130434782,
                                0.40901771336553905
                            ],
                            "start_time_in_video_in_sec": null,
                            "duration_in_video_in_sec": null
                        },
                        {
                            "user": {
                                "pk": "977097183",
                                "username": "gwenreecemakeupartist",
                                "full_name": "Gwen Reece",
                                "is_private": false,
                                "is_verified": false,
                                "profile_pic_url": "https://scontent-iad3-1.cdninstagram.com/vp/d6745db8761e92e15c34d44ad51acd82/5C1BFC12/t51.2885-19/s150x150/26872607_186292068784928_8279535729265082368_n.jpg",
                                "profile_pic_id": "1696350945703905357_977097183"
                            },
                            "position": [
                                0.19001610305958103,
                                0.31320450885668205
                            ],
                            "start_time_in_video_in_sec": null,
                            "duration_in_video_in_sec": null
                        }
                    ]
                }
            }
        ],
        "location": {
            "pk": "213385402",
            "name": "London, United Kingdom",
            "address": "",
            "city": "",
            "short_name": "London",
            "lng": -0.12731805236353,
            "lat": 51.507114863624,
            "external_source": "facebook_places",
            "facebook_places_id": "106078429431815"
        },
        "lat": 51.507114863624,
        "lng": -0.12731805236353,
        "user": {
            "pk": "2261848765",
            "username": "rektmag",
            "full_name": "REKT",
            "is_private": false,
            "profile_pic_url": "https://scontent-iad3-1.cdninstagram.com/vp/9ab56451e1f79ec951bf7b705322f1c1/5C399D73/t51.2885-19/s150x150/26320599_1849591135082144_3103955624820473856_n.jpg",
            "profile_pic_id": "1692769662418409713_2261848765",
            "friendship_status": {
                "following": true,
                "outgoing_request": false,
                "is_bestie": false
            },
            "is_verified": false,
            "has_anonymous_profile_picture": false,
            "reel_auto_archive": "on",
            "is_unpublished": false,
            "is_favorite": false
        },
        "can_viewer_reshare": true,
        "caption": {
            "pk": "17887906123026532",
            "user_id": "2261848765",
            "text": "That Time I Danced All Day \ud83d\udc83\ud83c\udffb\nNow up on www.rektmag.net\n@aisling_tara captured by @jtuliniemi \n#rektmag #dance #body #shape #form #bnw #expression",
            "type": 1,
            "created_at": "1499717881",
            "created_at_utc": "1499717881",
            "content_type": "comment",
            "status": "Active",
            "bit_flags": 0,
            "user": {
                "pk": "2261848765",
                "username": "rektmag",
                "full_name": "REKT",
                "is_private": false,
                "profile_pic_url": "https://scontent-iad3-1.cdninstagram.com/vp/9ab56451e1f79ec951bf7b705322f1c1/5C399D73/t51.2885-19/s150x150/26320599_1849591135082144_3103955624820473856_n.jpg",
                "profile_pic_id": "1692769662418409713_2261848765",
                "friendship_status": {
                    "following": true,
                    "outgoing_request": false,
                    "is_bestie": false
                },
                "is_verified": false,
                "has_anonymous_profile_picture": false,
                "reel_auto_archive": "on",
                "is_unpublished": false,
                "is_favorite": false
            },
            "did_report_as_spam": false,
            "media_id": "1556068827723262974"
        },
        "caption_is_edited": false,
        "like_count": 3358,
        "has_liked": true,
        "photo_of_you": false,
        "usertags": {
            "in": [
                {
                    "user": {
                        "pk": "30978460",
                        "username": "jtuliniemi",
                        "full_name": "J. Tuliniemi",
                        "is_private": false,
                        "is_verified": false,
                        "profile_pic_url": "https://scontent-iad3-1.cdninstagram.com/vp/e7f8ec77099c0ec94121942928147ca2/5C058092/t51.2885-19/s150x150/15403531_1355211254499134_5786638901376450560_a.jpg",
                        "profile_pic_id": "1416978428045228714_30978460"
                    },
                    "position": [
                        0.19645731460645,
                        0.135265700483091
                    ],
                    "start_time_in_video_in_sec": null,
                    "duration_in_video_in_sec": null
                },
                {
                    "user": {
                        "pk": "359597261",
                        "username": "aisling_tara",
                        "full_name": "Aisling Tara",
                        "is_private": false,
                        "is_verified": false,
                        "profile_pic_url": "https://scontent-iad3-1.cdninstagram.com/vp/98f9b33736b017df63cce70d60c88e82/5BFD93C9/t51.2885-19/s150x150/33545973_260793151146887_3930585281379434496_n.jpg",
                        "profile_pic_id": "1803730515250779444_359597261"
                    },
                    "position": [
                        0.496779363512417,
                        0.547504001193576
                    ],
                    "start_time_in_video_in_sec": null,
                    "duration_in_video_in_sec": null
                },
                {
                    "user": {
                        "pk": "977097183",
                        "username": "gwenreecemakeupartist",
                        "full_name": "Gwen Reece",
                        "is_private": false,
                        "is_verified": false,
                        "profile_pic_url": "https://scontent-iad3-1.cdninstagram.com/vp/d6745db8761e92e15c34d44ad51acd82/5C1BFC12/t51.2885-19/s150x150/26872607_186292068784928_8279535729265082368_n.jpg",
                        "profile_pic_id": "1696350945703905357_977097183"
                    },
                    "position": [
                        0.177133643108865,
                        0.349436368343334
                    ],
                    "start_time_in_video_in_sec": null,
                    "duration_in_video_in_sec": null
                }
            ]
        },
        "can_viewer_save": true,
        "has_viewer_saved": true,
        "saved_collection_ids": [
            "17887886089047035"
        ],
        "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiMGEwNGI1MGZiYzMxNGMzZDgwYTQwMDU3MDQ1YTU2ZTQxNTU2MDY4ODI3NzIzMjYyOTc0Iiwic2VydmVyX3Rva2VuIjoiMTUzNDk4NzEzMDQ4MnwxNTU2MDY4ODI3NzIzMjYyOTc0fDIwNjcyNzU3MnwwNjU3MTkxM2UxYzViYjhiYmJhMDg5MjM0ZGZhN2RhZDk2NTA4YTg3NGExN2QyOWZlNTNhNzYwMjZmMDNlNmZkIn0sInNpZ25hdHVyZSI6IiJ9"
    }
}"""
VIDEO_JSON = r"""{
    "media": {
        "taken_at": "1502127452",
        "pk": "1576281775188357251",
        "id": "1576281775188357251_40268558",
        "device_timestamp": "1502127433",
        "media_type": 2,
        "code": "BXgE-xMBjCD",
        "client_cache_key": "MTU3NjI4MTc3NTE4ODM1NzI1MQ==.2",
        "filter_type": 0,
        "comment_likes_enabled": true,
        "comment_threading_enabled": true,
        "has_more_comments": true,
        "next_max_id": "17893440082038823",
        "max_num_visible_preview_comments": 2,
        "preview_comments": [
            {
                "pk": "17892834364052859",
                "user_id": "21333279",
                "text": "That's your favourite dance I've ever done",
                "type": 0,
                "created_at": "1502190196",
                "created_at_utc": "1502190196",
                "content_type": "comment",
                "status": "Active",
                "bit_flags": 0,
                "user": {
                    "pk": "21333279",
                    "username": "ediebcampbell",
                    "full_name": "Edie Campbell",
                    "is_private": false,
                    "is_verified": false,
                    "profile_pic_url": "https://scontent-iad3-1.cdninstagram.com/vp/0f57a5d1130edea2674a915b63cdbcfa/5BF8F3CC/t51.2885-19/s150x150/21149834_1459076594128439_6247246729096200192_a.jpg",
                    "profile_pic_id": "1592964290288829295_21333279"
                },
                "did_report_as_spam": false,
                "media_id": "1576281775188357251"
            },
            {
                "pk": "17893440082038823",
                "user_id": "4047109720",
                "text": "cute pic see m0del @NATASHAGALKINA",
                "type": 0,
                "created_at": "1502203431",
                "created_at_utc": "1502203431",
                "content_type": "comment",
                "status": "Active",
                "bit_flags": 0,
                "user": {
                    "pk": "4047109720",
                    "username": "art_calligraphy_diy",
                    "full_name": "Art Calligraphy",
                    "is_private": false,
                    "is_verified": false,
                    "profile_pic_url": "https://scontent-iad3-1.cdninstagram.com/vp/595fa96fc6c12f23f08ccbec2d0f6b4f/5C02DBBA/t51.2885-19/s150x150/16789277_434439926909977_4034173248244547584_a.jpg",
                    "profile_pic_id": "1457864162381952051_4047109720"
                },
                "did_report_as_spam": false,
                "media_id": "1576281775188357251"
            }
        ],
        "can_view_more_preview_comments": true,
        "comment_count": 10,
        "inline_composer_display_condition": "impression_trigger",
        "image_versions2": {
            "candidates": [
                {
                    "width": 640,
                    "height": 640,
                    "url": "https://scontent-iad3-1.cdninstagram.com/vp/61f5297b4817e58aa99bd794d031e86e/5B8022E9/t51.2885-15/e15/s640x640/20633552_502933673377392_6573004124298674176_n.jpg?ig_cache_key=MTU3NjI4MTc3NTE4ODM1NzI1MQ%3D%3D.2"
                },
                {
                    "width": 240,
                    "height": 240,
                    "url": "https://scontent-iad3-1.cdninstagram.com/vp/88b460bcad2aabbbf29dce588c76c4f1/5B8073FC/t51.2885-15/e15/s240x240/20633552_502933673377392_6573004124298674176_n.jpg?ig_cache_key=MTU3NjI4MTc3NTE4ODM1NzI1MQ%3D%3D.2"
                }
            ]
        },
        "original_width": 720,
        "original_height": 720,
        "is_dash_eligible": 1,
        "video_dash_manifest": "<MPD xmlns=\"urn:mpeg:dash:schema:mpd:2011\" minBufferTime=\"PT1.500S\" type=\"static\" mediaPresentationDuration=\"PT0H0M11.912S\" maxSegmentDuration=\"PT0H0M2.000S\" profiles=\"urn:mpeg:dash:profile:isoff-on-demand:2011,http://dashif.org/guidelines/dash264\"><Period duration=\"PT0H0M11.912S\"><AdaptationSet segmentAlignment=\"true\" maxWidth=\"720\" maxHeight=\"720\" maxFrameRate=\"30\" par=\"1:1\" lang=\"und\" subsegmentAlignment=\"true\" subsegmentStartsWithSAP=\"1\"><Representation id=\"17868011995180315vd\" mimeType=\"video/mp4\" codecs=\"avc1.4d401e\" width=\"640\" height=\"640\" frameRate=\"30\" sar=\"1:1\" startWithSAP=\"1\" bandwidth=\"811860\" FBQualityClass=\"sd\" FBQualityLabel=\"640w\"><BaseURL>https://scontent-iad3-1.cdninstagram.com/vp/debde259a59e9f4916877e3e483b4faa/5B803267/t50.2886-16/20710496_258294171333038_8633080862793007104_n.mp4</BaseURL><SegmentBase indexRangeExact=\"true\" indexRange=\"911-1014\"><Initialization range=\"0-910\"/></SegmentBase></Representation><Representation id=\"17877670486085093v\" mimeType=\"video/mp4\" codecs=\"avc1.4d401e\" width=\"720\" height=\"720\" frameRate=\"30\" sar=\"1:1\" startWithSAP=\"1\" bandwidth=\"1183532\" FBQualityClass=\"hd\" FBQualityLabel=\"720w\"><BaseURL>https://scontent-iad3-1.cdninstagram.com/vp/d3a8823249a28d4444a4d68c1b439a72/5B800A53/t50.2886-16/20709989_113807085946954_6975166994832162816_n.mp4</BaseURL><SegmentBase indexRangeExact=\"true\" indexRange=\"911-1014\"><Initialization range=\"0-910\"/></SegmentBase></Representation><Representation id=\"17867791741155065v\" mimeType=\"video/mp4\" codecs=\"avc1.4d401e\" width=\"480\" height=\"480\" frameRate=\"30\" sar=\"1:1\" startWithSAP=\"1\" bandwidth=\"512951\" FBQualityClass=\"sd\" FBQualityLabel=\"480w\"><BaseURL>https://scontent-iad3-1.cdninstagram.com/vp/5586040fa5ee4833ac7b7b7e4e004673/5B8021BB/t50.2886-16/20677572_1842785289372262_8536295660268290048_n.mp4</BaseURL><SegmentBase indexRangeExact=\"true\" indexRange=\"911-1014\"><Initialization range=\"0-910\"/></SegmentBase></Representation><Representation id=\"17867621953182700v\" mimeType=\"video/mp4\" codecs=\"avc1.4d401e\" width=\"320\" height=\"320\" frameRate=\"30\" sar=\"1:1\" startWithSAP=\"1\" bandwidth=\"282750\" FBQualityClass=\"sd\" FBQualityLabel=\"320w\"><BaseURL>https://scontent-iad3-1.cdninstagram.com/vp/7b6b4297e76600e95a611eeda9242598/5B804CEE/t50.2886-16/20709962_134562070480358_4968326363086848000_n.mp4</BaseURL><SegmentBase indexRangeExact=\"true\" indexRange=\"911-1014\"><Initialization range=\"0-910\"/></SegmentBase></Representation></AdaptationSet><AdaptationSet segmentAlignment=\"true\" lang=\"und\" subsegmentAlignment=\"true\" subsegmentStartsWithSAP=\"1\"><Representation id=\"17868221647150291ad\" mimeType=\"audio/mp4\" codecs=\"mp4a.40.2\" audioSamplingRate=\"44100\" startWithSAP=\"1\" bandwidth=\"66550\"><AudioChannelConfiguration schemeIdUri=\"urn:mpeg:dash:23003:3:audio_channel_configuration:2011\" value=\"2\"/><BaseURL>https://scontent-iad3-1.cdninstagram.com/vp/94baf853fb513e0353f0e4dcb41ac75f/5B80405A/t50.2886-16/20677768_164394267460348_6594480820499513344_n.mp4</BaseURL><SegmentBase indexRangeExact=\"true\" indexRange=\"832-935\"><Initialization range=\"0-831\"/></SegmentBase></Representation></AdaptationSet></Period></MPD>",
        "number_of_qualities": 4,
        "video_versions": [
            {
                "type": 101,
                "width": 640,
                "height": 640,
                "url": "https://scontent-iad3-1.cdninstagram.com/vp/809a3b7335ef9caf03e10b03c491b91a/5B7FF7F6/t50.2886-16/20730290_137619573507645_7996592934596116480_n.mp4",
                "id": "0"
            },
            {
                "type": 103,
                "width": 480,
                "height": 480,
                "url": "https://scontent-iad3-1.cdninstagram.com/vp/9514efe36fc081fb6799d969090e0119/5B8000E8/t50.2886-16/20678064_2001113480122067_6136301912749768704_n.mp4",
                "id": "0"
            },
            {
                "type": 102,
                "width": 480,
                "height": 480,
                "url": "https://scontent-iad3-1.cdninstagram.com/vp/9514efe36fc081fb6799d969090e0119/5B8000E8/t50.2886-16/20678064_2001113480122067_6136301912749768704_n.mp4",
                "id": "0"
            }
        ],
        "has_audio": true,
        "video_duration": 11.76,
        "view_count": 18073,
        "user": {
            "pk": "40268558",
            "username": "kegrand",
            "full_name": "Katie Eleanor Grand",
            "is_private": false,
            "profile_pic_url": "https://scontent-iad3-1.cdninstagram.com/vp/f25aac2a19fc0e68edf29d6611bec0e5/5C14DEF2/t51.2885-19/s150x150/13643511_705893552907612_1359669151_a.jpg",
            "profile_pic_id": "1291402491912570156_40268558",
            "friendship_status": {
                "following": true,
                "outgoing_request": false,
                "is_bestie": false
            },
            "is_verified": true,
            "has_anonymous_profile_picture": false,
            "reel_auto_archive": "on",
            "is_unpublished": false,
            "is_favorite": false
        },
        "can_viewer_reshare": true,
        "caption": {
            "pk": "17879616295123158",
            "user_id": "40268558",
            "text": "Cara and Edie from when they both had more HAIR \ud83e\udd23\ud83e\udd23\ud83e\udd23",
            "type": 1,
            "created_at": "1502127452",
            "created_at_utc": "1502127452",
            "content_type": "comment",
            "status": "Active",
            "bit_flags": 0,
            "user": {
                "pk": "40268558",
                "username": "kegrand",
                "full_name": "Katie Eleanor Grand",
                "is_private": false,
                "profile_pic_url": "https://scontent-iad3-1.cdninstagram.com/vp/f25aac2a19fc0e68edf29d6611bec0e5/5C14DEF2/t51.2885-19/s150x150/13643511_705893552907612_1359669151_a.jpg",
                "profile_pic_id": "1291402491912570156_40268558",
                "friendship_status": {
                    "following": true,
                    "outgoing_request": false,
                    "is_bestie": false
                },
                "is_verified": true,
                "has_anonymous_profile_picture": false,
                "reel_auto_archive": "on",
                "is_unpublished": false,
                "is_favorite": false
            },
            "did_report_as_spam": false,
            "media_id": "1576281775188357251"
        },
        "caption_is_edited": false,
        "like_count": 2040,
        "has_liked": true,
        "photo_of_you": false,
        "can_viewer_save": true,
        "has_viewer_saved": true,
        "saved_collection_ids": [
            "17865649783171012"
        ],
        "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiMDc5ODM3YzIyMmFiNDhmY2IwM2ExYzAxZDViZjQyODYxNTc2MjgxNzc1MTg4MzU3MjUxIiwic2VydmVyX3Rva2VuIjoiMTUzNDk4MzU1OTQ3NHwxNTc2MjgxNzc1MTg4MzU3MjUxfDIwNjcyNzU3Mnw1NjcyOGUwNDMyYzFkMGUzZDk0NTg2MTBkZjdmMDI2ZjEwMjlkYWVkZjZiMDZkN2UxY2YxNjAyNWNmMzlhMTlmIn0sInNpZ25hdHVyZSI6IiJ9"
    }
}"""
IMAGE_JSON = r"""{
    "media": {
        "taken_at": "1447118663",
        "pk": "1114834611136085885",
        "id": "1114834611136085885_1435801262",
        "device_timestamp": "1447118507894",
        "media_type": 1,
        "code": "94sCwUE799",
        "client_cache_key": "MTExNDgzNDYxMTEzNjA4NTg4NQ==.2",
        "filter_type": 0,
        "comment_likes_enabled": true,
        "comment_threading_enabled": true,
        "has_more_comments": true,
        "next_max_id": "17894911774110732",
        "max_num_visible_preview_comments": 2,
        "preview_comments": [
            {
                "pk": "17881794403147543",
                "user_id": "410713076",
                "text": "Project final ni kene buat room w a view so thanks bg idea kakya hahahahaha @surayaarifin",
                "type": 0,
                "created_at": "1510409070",
                "created_at_utc": "1510409070",
                "content_type": "comment",
                "status": "Active",
                "bit_flags": 0,
                "user": {
                    "pk": "410713076",
                    "username": "alyadlinafynn",
                    "full_name": "IIIIIIIIIIIIIIIIIIIII",
                    "is_private": true,
                    "is_verified": false,
                    "profile_pic_url": "https://scontent-iad3-1.cdninstagram.com/vp/5eab433808b7cc01efc40fa3820a8cb9/5C1A1599/t51.2885-19/s150x150/15538712_182241805583824_7944391537008312320_a.jpg",
                    "profile_pic_id": "1417519816960465571_410713076"
                },
                "did_report_as_spam": false,
                "media_id": "1114834611136085885",
                "has_translation": true
            },
            {
                "pk": "17894911774110732",
                "user_id": "34888132",
                "text": "@alyadlinafynn goodluck!! Buat yg paling gempak please bye",
                "type": 2,
                "created_at": "1510409125",
                "created_at_utc": "1510409125",
                "content_type": "comment",
                "status": "Active",
                "bit_flags": 0,
                "user": {
                    "pk": "34888132",
                    "username": "surayaarifin",
                    "full_name": "",
                    "is_private": true,
                    "is_verified": false,
                    "profile_pic_url": "https://scontent-iad3-1.cdninstagram.com/vp/1c1a3d147cbd1c6b15891982f4aa8903/5C38AC86/t51.2885-19/s150x150/38520389_226813628001964_721075715658743808_n.jpg",
                    "profile_pic_id": "1847081806600738761_34888132"
                },
                "did_report_as_spam": false,
                "media_id": "1114834611136085885",
                "has_translation": true,
                "parent_comment_id": "17881794403147543"
            }
        ],
        "can_view_more_preview_comments": true,
        "comment_count": 11,
        "inline_composer_display_condition": "impression_trigger",
        "image_versions2": {
            "candidates": [
                {
                    "width": 640,
                    "height": 473,
                    "url": "https://scontent-iad3-1.cdninstagram.com/vp/e6501bbf26e70ffbff34ac00b219429a/5BFB814F/t51.2885-15/e15/12224231_897785673633388_1507672615_n.jpg?ig_cache_key=MTExNDgzNDYxMTEzNjA4NTg4NQ%3D%3D.2"
                },
                {
                    "width": 240,
                    "height": 177,
                    "url": "https://scontent-iad3-1.cdninstagram.com/vp/fb8437bf4ffd06894c4ad7e0cddf9bc7/5C0B275E/t51.2885-15/e15/s240x240/12224231_897785673633388_1507672615_n.jpg?ig_cache_key=MTExNDgzNDYxMTEzNjA4NTg4NQ%3D%3D.2"
                }
            ]
        },
        "original_width": 640,
        "original_height": 473,
        "user": {
            "pk": "1435801262",
            "username": "equitone_facade",
            "full_name": "Equitone",
            "is_private": false,
            "profile_pic_url": "https://scontent-iad3-1.cdninstagram.com/vp/a92572c3f73d3c63ff24cf1a8568f611/5BFCD531/t51.2885-19/s150x150/12132678_1739118912982644_1105738301_a.jpg",
            "friendship_status": {
                "following": true,
                "outgoing_request": false,
                "is_bestie": false
            },
            "is_verified": false,
            "has_anonymous_profile_picture": false,
            "reel_auto_archive": "unset",
            "is_unpublished": false,
            "is_favorite": false
        },
        "can_viewer_reshare": true,
        "caption": {
            "pk": "17843518111122582",
            "user_id": "1435801262",
            "text": "Ashton college reception. arch: GA studio. EQUITONE facade materials. #architecture #facade #material",
            "type": 1,
            "created_at": "1447118663",
            "created_at_utc": "1447118663",
            "content_type": "comment",
            "status": "Active",
            "bit_flags": 0,
            "user": {
                "pk": "1435801262",
                "username": "equitone_facade",
                "full_name": "Equitone",
                "is_private": false,
                "profile_pic_url": "https://scontent-iad3-1.cdninstagram.com/vp/a92572c3f73d3c63ff24cf1a8568f611/5BFCD531/t51.2885-19/s150x150/12132678_1739118912982644_1105738301_a.jpg",
                "friendship_status": {
                    "following": true,
                    "outgoing_request": false,
                    "is_bestie": false
                },
                "is_verified": false,
                "has_anonymous_profile_picture": false,
                "reel_auto_archive": "unset",
                "is_unpublished": false,
                "is_favorite": false
            },
            "did_report_as_spam": false,
            "media_id": "1114834611136085885"
        },
        "caption_is_edited": false,
        "like_count": 289,
        "has_liked": false,
        "photo_of_you": false,
        "can_viewer_save": true,
        "has_viewer_saved": true,
        "saved_collection_ids": [
            "17878861282073803"
        ],
        "organic_tracking_token": "eyJ2ZXJzaW9uIjo1LCJwYXlsb2FkIjp7ImlzX2FuYWx5dGljc190cmFja2VkIjp0cnVlLCJ1dWlkIjoiODExMDIxNGQ2NWMzNGFlYWFjY2JiNGY4NTQyMTE1ODUxMTE0ODM0NjExMTM2MDg1ODg1Iiwic2VydmVyX3Rva2VuIjoiMTUzNDk4NDUyMTE0OXwxMTE0ODM0NjExMTM2MDg1ODg1fDIwNjcyNzU3MnwyOTgwYTlmODQ3NzA2Y2FkNDkwZWIxMjk3MTYxYzM0Mzc5MjAzZmI2M2RjMWVjMWRkZjVhNDBlYWMyNGY2ZTVkIn0sInNpZ25hdHVyZSI6IiJ9"
    }
}"""


def test_init_tables():
    """Test igsync's ability to initialize tables without raising errors."""
    DB.inittables()


def test_save_post():
    """Test igsync's ability to save JSON posts to a database without raising
    errors."""
    for post in (CAROUSEL_JSON, VIDEO_JSON, IMAGE_JSON):
        DB.save_post(post)


def test_collection_sync():
    """Test igsync's ability to sync collection names."""
    DB.sync_collection_names(DB.get_anonymous_collections())


def main():
    test_init_tables()
    test_save_post()
    test_collection_sync()

if __name__ == "__main__":
    main()
