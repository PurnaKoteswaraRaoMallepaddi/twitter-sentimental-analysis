# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 18:48:40 2017

@author: purna
"""

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
#import pandas as pd

ckey = 'YOUR OWN CREDENTIALS'
csecret = 'YOUR OWN CREDENTIALS'
atoken = 'YOUR OWN CREDENTIALS'
asecret = 'YOUR OWN CREDENTIALS'

class listener(StreamListener):
    def on_data(self, data):
        #try: 
            tweet = data.split(',"text":"')[1].split('","source')[0]
            #print(tweet)
            saveThis = str(time.time())+'::'+tweet
            saveFile = open('twitdb1.csv','a')
            saveFile.write(saveThis)
            #print(saveThis)
            saveFile.write('\n')
            saveFile.close()
            return True
        #except BaseException, e:
            #print('failed ondata',str(e))
            #time.sleep(5)
    def on_error(self, status):
        print(status)
    
auth =  OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track = ["happy","enjoy","masti","holiday","chill","full","party","sex","ohhhh"])  #you can add what ever you want to add