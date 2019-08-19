# TWIT Downloader #
A series of scripts for downloading content from TWIT.tv or from the website of one of the hosts

A parent object (twit_show.py) will give a basic description of a podcast's assets, whith individual podcasts being a child of this object with show-specific information, this is because there are situations (eg show notes) that are handled differently for every podcast

The Parent object will be able to handle downloading content hosted by TWIT (vidoe and audio streams and YouTube)
