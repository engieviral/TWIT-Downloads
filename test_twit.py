#! python3

# twit_test.py - class used for testing twit_show.py

import twit_show

TheTechGuy = twit_show.podcast('https://twit.tv/ttg')
print(TheTechGuy.show)

AllAboutAndroid = twit_show.podcast('http://www.twit.tv/aaa')
print(AllAboutAndroid.show)