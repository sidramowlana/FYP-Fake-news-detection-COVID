from .access_train_dataset import *
import pandas as pd
import numpy as np
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

stop_words = set(stopwords.words('english'))
tfidf_vectorizer = TfidfVectorizer(stop_words="english", max_df=0.65)


class feature_extraction_class:

    def __init__(self):
        pass

    def tfidf_text(self, preprocessed_text):
        global tfidf_vectorizer
        global stopwords
        csv_label = access_dataset_class()
        factcheck = csv_label.read_label_csv()
        a_train, a_test, b_train, b_test = train_test_split(
            preprocessed_text, factcheck, test_size=0.15, random_state=8)
        tfidf_train = tfidf_vectorizer.fit_transform(a_train)
        tfidf_test = tfidf_vectorizer.transform(a_test)
        # Save the vectorizer
        vec_file = os.path.normpath(
            os.getcwd() + os.sep)+'\model\Vectorizer.pickle'
        pickle.dump(tfidf_vectorizer, open(vec_file, 'wb'))
        return tfidf_train, b_train, tfidf_test, b_test

    def new_tfidf(self, new_text):
        # load the vectorizer
        loaded_vectorizer = pickle.load(open(os.path.normpath(
            os.getcwd() + os.sep)+'\model\Vectorizer.pickle', 'rb'))
        print("here")
        print(new_text)
        vectorized_sentence = loaded_vectorizer.transform(new_text)
        print(vectorized_sentence)
        return vectorized_sentence
