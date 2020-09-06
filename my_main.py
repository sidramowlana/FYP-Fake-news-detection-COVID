import twitter_extractor
import pre_process
import feature_extraction
import access_train_dataset
import train_model

import pandas as pd
import numpy as np

url = "https://twitter.com/BBCBreaking/status/1299016807660036103"

def main_load(url):
    text = tweet_retrievel(url)
    return text

def tweet_retrievel(url):
    twitter_api = twitter_extractor.twitter_extractor_class()
    twitter_api.create_tweepy_api()
    api = twitter_api.create_tweepy_api()
    new_text = twitter_api.get_tweet_post_id_text(api,url)
    return new_text

def train_my_model():
    train = train_model.train_model_class()
    text = access_train_dataset.access_dataset_class().read_text_csv()     
    processed = pre_process.pre_process_class()
    final_text = processed.pre_process_text(text)
    extracted = feature_extraction.feature_extraction_class(final_text)    
    result = extracted.tfidf_text(final_text)
    train.train_start_NB(result)
    # train.train_start_Voting_Classifier(result)
    # train.train_start_RF(result)
    # train.train_start_SVM(result)
    # train.train_start_KNN(result)
    print("saved model")
        

def predict_new_text(text):
    print("begin")
    train = train_model.train_model_class()
    processed = pre_process.pre_process_class()
    final_text = processed.pre_process_text([text])
    extracted = feature_extraction.feature_extraction_class(final_text)
    result = extracted.tfidf_text(final_text)    
    b = np.resize(result, (len(result),18855))
    new_result = train.load_model(b)
    return new_result

def validate_tweet_url(url):
    print("Initializing the main method!")    
    text = main_load(url)
    new_text = text[0]
    test_text = new_text.split('\n')
    return predict_new_text(test_text)

if __name__ == "__main__":
    print("Initializing the main method!")  
    ## load url and check  
    # text = main_load(url)
    # new_text = text[0]
    # print(new_text)
    # new_result = predict_new_text(new_text)
    # print(new_result)

    print("*******************************************")
    train_my_model()
    print("main train")

    ## my check
    # fake = "Using a hair dryer to breathe in hot air can cure COVID-19 and stop its spread."
    # real ="Frequent or excessive alcohol consumption can increase your risk of health problems due to frequent usage"
    # new_text = 'South Australian COVID-19 update 29/8/20. For more information go to \n https://buff.ly/2IBPz2x or contact the \n South Australian COVID-19 \n Information Line on 1800 253 787.'
    # result = predict_new_text(new_text)
    # print("final result")
    # print(result)


