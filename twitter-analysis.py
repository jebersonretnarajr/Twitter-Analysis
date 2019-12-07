# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 12:42:10 2019

@author: admin
"""

# API Authentication 

# Importing TWEEPY Library
import tweepy

# Store OAuth authentication credentials in relevant variables
access_token = "938981413260468228-hjf9NqLdChXibPhZvqtVvERdfJWMnEr"
access_token_secret = "IgEyUiw505a4rstiXv1uHaFcAQGMdMV0FFfi2VWuWcyfa"
consumer_key = "nN8IZ9h4lWt00NR7iAr8KjVjE"
consumer_secret = "w7qG3IOtjvyzah1USvpCj72FqhQWnRR81fODGgGpit4tAQVgCq"

# Pass OAuth details to tweepy's OAuth handler
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Streaming Tweets
#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)

# Initialize Stream listener
l = MyStreamListener()

# Create you Stream object with authentication
stream = tweepy.Stream(auth, l)

# Filter Twitter Streams to capture data by the keywords:
stream.filter(track = ['clinton', 'trump', 'sanders', 'cruz'])