from ML import train_model, twitter_extractor, access_train_dataset, pre_process, feature_extraction
import pandas as pd
import numpy as np
url = "https://twitter.com/BBCBreaking/status/1299016807660036103"


# when the postid is passed for the text
def tweet_text_retrievel(postId):
    twitter_api = twitter_extractor.twitter_extractor_class()
    twitter_api.create_tweepy_api()
    api = twitter_api.create_tweepy_api()
    new_text = twitter_api.get_tweet_post_id_text(api, postId)
    return new_text

# get the tweet details for the postid
def tweet_data_retrievel(postId):
    twitter_api = twitter_extractor.twitter_extractor_class()
    twitter_api.create_tweepy_api()
    api = twitter_api.create_tweepy_api()
    tweet_data = twitter_api.get_tweet_data(api, postId)
    return tweet_data

def train_my_model():
    train = train_model.train_model_class()
    text = access_train_dataset.access_dataset_class().read_text_csv()
    processed = pre_process.pre_process_class()
    final_text = processed.pre_process_text(text)
    print(final_text)
    extracted = feature_extraction.feature_extraction_class()
    tfidf_train, b_train, tfidf_test, b_test = extracted.tfidf_text(final_text)
    train.train_passve_aggresive_classifier(
        tfidf_train, b_train, tfidf_test, b_test)
    print("saved model")
    
def predict_new_text(text):
    print("begin")
    train = train_model.train_model_class()
    processed = pre_process.pre_process_class()
    final_text = processed.pre_process_text(text)
    print(final_text, "predict")
    extracted = feature_extraction.feature_extraction_class()
    vectorized_result = extracted.vectorize_text(final_text)
    new_result = train.load_model(vectorized_result)
    return new_result


def validate_tweet_text(postId):
    tweet_text = tweet_text_retrievel(postId);
    train = train_model.train_model_class()
    processed = pre_process.pre_process_class()
    final_text = processed.pre_process_text(tweet_text)
    extracted = feature_extraction.feature_extraction_class()
    result = extracted.vectorize_text(final_text)
    new_result = train.load_model(result)
    return new_result


# if __name__ == "__main__":
#     print("Initializing the main method!")
#     # print("*****************************train*****************************")
#     # train_my_model()
#     # print("main train")

#     print("*****************************validate*****************************")
#     tweet_text = tweet_retrievel(url)
#     # result = predict_new_text(tweet_text)
#     print(tweet_text)
#     print("*****************************end*****************************")
