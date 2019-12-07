# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 16:56:47 2019

@author: admin
"""

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
#Variables that contains the user credentials to access Twitter API
access_token = "938981413260468228-hjf9NqLdChXibPhZvqtVvERdfJWMnEr"
access_token_secret = "IgEyUiw505a4rstiXv1uHaFcAQGMdMV0FFfi2VWuWcyfa"
consumer_key = "nN8IZ9h4lWt00NR7iAr8KjVjE"
consumer_secret = "w7qG3IOtjvyzah1USvpCj72FqhQWnRR81fODGgGpit4tAQVgCq"
#This is a basic listener that just prints received tweets to stdout.
class StdOutListener (StreamListener):
    def on_data(self, data):
        print(data)
        return True
    def on_error(self, status):
        print(status)
if __name__ == '__main__':
            # This handles Twitter authentication and the connection to Twitter Streaming API
            l = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
stream = Stream(auth, l)
        #This line filter Twitter Streams to capture data by the keywords: 'python', 'java','javascript'
stream.filter(track=['modi'])