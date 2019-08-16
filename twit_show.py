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
    dl_links = {
        'HD-Video' : 'none',
        'SD-Video-Lg' : 'none',
        'SD-Video-Sm' : 'none',
        'Audio' : 'none'
        'Youtube' : 'none'
    }

