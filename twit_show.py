#! python3

# twit_show.py - A class that defines a generic TWIT show podcast.

import requests
import bs4
import re

class podcast():
    # Class variables
    show = '' # short end of url (used in url for content of shows)
    website = 'https://www.twit.tv'
    hosts = ['Leo Laporte']
    hosts_site = ['https://www.twit.tv']
    dl_types = {    # dict with the type of download as the key and the location of the download as the value
        'HD-Video' : {
            'pre' : 'https://media.blubrry.com/the_tech_guy_video_hd/www.podtrac.com/pts/redirect.mp4/cdn.twit.tv/video/',
            'post' : '_h264m_1280x720_1872.mp4'
        },
        'SD-Video-Lg' : {
            'pre' : 'https://media.blubrry.com/the_tech_guy_video_hd/www.podtrac.com/pts/redirect.mp4/cdn.twit.tv/video/',
            'post' : '_h264m_864x480_500.mp4'
        },
        'SD-Video-Sm' : { 
            'pre' : 'https://media.blubrry.com/the_tech_guy_video_hd/www.podtrac.com/pts/redirect.mp4/cdn.twit.tv/video/',
            'post' : '_h264b_640x368_256.mp4'
        },
        'Audio' : {
            'pre' : 'https://media.blubrry.com/35016/www.podtrac.com/pts/redirect.mp3/cdn.twit.tv/audio',
            'post' : '.mp3'
        },
        'Youtube' : 'https://youtu.be/'
    }
    latest_ep = 0 # The episode number of the most recenly published podcast, initialised to 0 - constructor to find latest
    
    # TODO : Constructor
    def __init__(self, url):
        """ Takes the short designation for the show url (ie /ttg, not /the-tech-guy) and builds the show object"""
        # Regex for the url
        showRE = re.compile("""
            ^(http[s]?://)                  # Grab the starting "http://" or "https://"
            ((www\.)?twit\.tv/)                # Grab the main TWIT url with or without the "www."
            (.*)                            # Grab the show designator
            """,
            re.I | re.VERBOSE
        )
        match = showRE.match(url)
        if match is None:
            raise Exception('URL entered is not correct, should be "https://twit.tv/{short_show_name}"')
        else:
            self.show = match.group(4) # The group of the show designator

        self.website = url
        
        
    # TODO: Get dl_types addresses
    def _get_dl_types(self, url):
        pass
    
    # Get the hosts of the show
    def _get_hosts(self):
        pass

    # TODO: Get latest episode
    def _get_latest_ep(self):
        pass

    # TODO: Get Episode name from number
    def _get_ep_from_num(self, num):
        pass

    # TODO: Show Episode list (arg specifies how many episodes to show)
    def ep_list(self, start_ep, end_ep):
        pass

    # TODO: Download Content (arg for what type (show notes/audio/video) and what episode number)
    def getContent(self, content, start_ep, end_ep):
        pass

