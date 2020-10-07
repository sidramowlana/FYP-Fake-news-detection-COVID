import pandas as pd
import tweepy
import json
from pandas.io.json import json_normalize

class twitter_extractor_class:
    consumer_key= 'ttNZAW9X740rprP49SxPJjEUd'
    consumer_secret= 'CZNYaZMSo3sbvY2SF5dBhULs0ZGeRmz6jdFtURwtHLZlcDhq9i'
    access_token= '1254498561116590087-qCEVE0x0xzlFSuXjsClIYyziqPmvwN'
    access_token_secret= '23MVQvcpuVFYsraBjbMagzBn9nKEBh8ImdpkyhNdSYL0i'
    
    def create_tweepy_api(self):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        return tweepy.API(auth,parser=tweepy.parsers.JSONParser())

    def get_tweet_post_id_text(self, api, url):
        post_id = url.split("status/",1)[1] 
        tweet_object = api.get_status(post_id)
        tweet_text = [tweet_object["text"]]
        return tweet_text


