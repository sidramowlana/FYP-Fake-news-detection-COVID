import pandas as pd
import tweepy
import json
import database.db_models as db_models
from pandas.io.json import json_normalize


class twitter_extractor_class:
    consumer_key = 'ttNZAW9X740rprP49SxPJjEUd'
    consumer_secret = 'CZNYaZMSo3sbvY2SF5dBhULs0ZGeRmz6jdFtURwtHLZlcDhq9i'
    access_token = '1254498561116590087-qCEVE0x0xzlFSuXjsClIYyziqPmvwN'
    access_token_secret = '23MVQvcpuVFYsraBjbMagzBn9nKEBh8ImdpkyhNdSYL0i'

    def create_tweepy_api(self):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        return tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    # def get_tweet_post_id_text(self, api, postId):
    #     print(postId)
    #     tweet_object = api.get_status(postId)
    #     tweet_text = [tweet_object["text"]]
    #     return tweet_text

    def get_tweet_post_id_text(self,api,postId):
        try:
            tweet_object = api.get_status(postId)
            tweet_text = [tweet_object["text"]]
            return tweet_text
        except tweepy.TweepError as e:
            message = e.args[0][0]['message']    
            raise Exception(message)
        except Exception as e:
            raise Exception("Error occured while retrieving the tweet")

    def get_tweet_data(self, api, postId):
        tweet_object = api.get_status(postId)
        print(tweet_object)
        entities = tweet_object['entities']
        urls = entities['urls']
        user = tweet_object['user']
        tweetObj = db_models.Tweets(
            postId=tweet_object['id_str'],
            text=tweet_object['text'],
            scaled_image=user['profile_image_url_https'],
            screen_name=user['screen_name'],
            created_date=tweet_object['created_at'],
            followings=user['friends_count'],
            followers=user['followers_count'],
            likes=tweet_object['favorite_count']
        )
        return tweetObj.to_json()
