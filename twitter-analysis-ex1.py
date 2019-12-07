# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 12:42:10 2019

@author: admin
"""

# API Authentication 

# Importing TWEEPY Library
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

# Store OAuth authentication credentials in relevant variables
access_token = "938981413260468228-hjf9NqLdChXibPhZvqtVvERdfJWMnEr"
access_token_secret = "IgEyUiw505a4rstiXv1uHaFcAQGMdMV0FFfi2VWuWcyfa"
consumer_key = "nN8IZ9h4lWt00NR7iAr8KjVjE"
consumer_secret = "w7qG3IOtjvyzah1USvpCj72FqhQWnRR81fODGgGpit4tAQVgCq"

# Pass OAuth details to tweepy's OAuth handler
class listener(StreamListener):

    def on_data(self, data):
        print(data)
        return(True)

    def on_error(self, status):
        print(status)

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["modi"])