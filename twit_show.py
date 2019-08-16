#! python3

# twit_show.py - A class that defines a generic TWIT show podcast.  Designed to be a parent for the actual podcasts objects

import requests
import bs4
import re

class twit():
    # Class variables
    website = 'https://www.twit.tv'
    hosts = ['Leo Laporte']
    hosts_site = ['https://www.twit.tv']
    show_notes = 'none'
    dl_types = {    # dict with the type of download as the key and the location of the download as the value
        'HD-Video' : 'none',
        'SD-Video-Lg' : 'none',
        'SD-Video-Sm' : 'none',
        'Audio' : 'none'
        'Youtube' : 'none'
    }
    latest_ep = 0 # The episode number of the most recenly published podcast, initialised to 0 - constructor to find latest
    
    # TODO : Constructor

    # TODO: Get latest episode

    # TODO: Get Episode name from number

    # TODO: Show Episode list (arg specifies how many episodes to show)

    # TODO: Download Content (arg for what type (show notes/audio/video) and what episode number)

