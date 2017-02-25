# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 22:17:06 2016

@author: purna
#"""
import pandas as pd
import json
import oauth2 as oauth
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

consumer_key = 'YOUR OWN CREDENTIALS'
consumer_secret = 'YOUR OWN CREDENTIALS'

access_token = 'YOUR OWN CREDENTIALS'
access_token_secret = 'YOUR OWN CREDENTIALS'

consumer = oauth.Consumer(key=consumer_key,secret=consumer_secret)
acess_token = oauth.Token(key=access_token,secret=access_token_secret)
client = oauth.Client(consumer,access_token)

timeline_endpoint = "https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=	YOUR OWN SCREEN NAME &count=1"

response, data = client.request(timeline_endpoint)

tweets = json.loads(data)
for tweet in tweets:
    Q = tweet['text']
    #print(data)




#Q = ["my life ruined"]
stream = pd.read_csv('twitdb.csv')    #THIS CONTAINS THE DATA I GOT FROMTHE TWITTER
#print(spamset) 
spamset = stream.tweetsad 
 
       
bow = CountVectorizer()

A = bow.fit_transform(spamset)
print(spamset) 

print (bow.get_feature_names())




X = A.toarray()
#print(X)


Y = stream.y 
#print(Y)
from sklearn.naive_bayes import MultinomialNB  #USING NAIVE BAYS
Z=bow.transform(Q).toarray()
clf = MultinomialNB()
print(spamset) 
clf.fit(X, Y)

print(clf.predict(Z))

