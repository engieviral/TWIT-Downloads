#! python3

# twit_show.py - A class that defines a generic TWIT show podcast.

import requests
import bs4
import re

class podcast():
    # Class variables
    show = '' # short end of url (used in url for content of shows)
    website = 'https://www.twit.tv'
    hosts = {}
    latest_ep = 0 # The episode number of the most recenly published podcast, initialised to 0 - constructor to find latest
    episodes = {}
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

        self.soup = bs4.BeautifulSoup(requests.get(url).text, features='lxml' )
        
        show_link = self.soup.find('a', class_='cta')['href'] # link in the format "/episodes?filter[shows]=xxxx" where xxxx is the show code (4+ digits)
        show_code_re = re.compile( '(/episodes\?filter\[shows\]=)(.*)' ) # re to format the link into two groups to extract the show code
        show_code = show_code_re.match(show_link)
                
        ep_url = 'https://twit.tv/episodes?filter[shows]=' + show_code.group(2)
        
        all_eps_html = bs4.BeautifulSoup(requests.get(ep_url).text, features='lxml' )

        page_max = int(all_eps_html.find('input' , class_ ='page-number-input')['max']) + 1
        
        print('Getting Episodes . . . .\nPlease be patient, this might take a while for shows with many episodes')
        
        for page in range( 1 , page_max ):
            current_url = ep_url + '&page=' + str(page)
            all_eps_html = bs4.BeautifulSoup(requests.get(current_url).text, features='lxml' )   
            all_eps = all_eps_html.find_all( 'div' , class_ = 'episode item' )

            for result in all_eps:
                key = result.find('a')['href']
                value = result.find('a')['title']

                self.episodes.update({key: value})

        print('Episodes list collected')
        # with open('ep_list.txt', 'w') as f:
        #     f.write(str(list(self.episodes)))
        # f.close()
            
        
    # TODO: Get dl_types addresses
    def _update_dl_types(self, url):
        pass
    
    # Get the hosts of the show
    def _get_hosts(self):
        return {'Leo Laporte' : 'https://twit.tv/people/leo-laporte'}

    # TODO: Get latest episode
    def _get_latest_ep(self):
        pass
        
    # TODO: Get Episode name from number
    def _get_ep_from_num(self, num):
        pass

    # TODO: Show Episode list (arg specifies how many episodes to show)
    def ep_list(self, start_ep, num_eps):
        pass

    # TODO: Download Content (arg for what type (show notes/audio/video) and what episode number)
    def getContent(self, content, start_ep, end_ep):
        pass

