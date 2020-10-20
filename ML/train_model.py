from .access_train_dataset import *
import pickle
import pandas as pd
import numpy as np
from sklearn.metrics import classification_report
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import VotingClassifier
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
import itertools
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix


class train_model_class:
    def __init__(self):
        pass

    def train_passve_aggresive_classifier(self, tfidf_train, b_train, tfidf_test, b_test):
        pclass = PassiveAggressiveClassifier(max_iter=60)
        pclass.fit(tfidf_train, b_train)
        b_pred = pclass.predict(tfidf_test)
        factcheckscore = accuracy_score(b_test, b_pred)
        print(f"Accuracy Is {round(factcheckscore*100,2)}%")
        return self.save_model(pclass)

    def train_start_NB(self, x):
        x = x
        csv_label = access_dataset_class()
        y = csv_label.read_label_csv()
        x_train, x_test, y_train, y_test = train_test_split(
            x, y, shuffle=False, stratify=None, train_size=0.6, test_size=0.4)
        a = np.array(x_test)
        df = pd.DataFrame(a)
        print("shape")
        print(df.shape)
        model = MultinomialNB()
        model.fit(x_train, y_train)
        print("scores train")
        print(model.score(x_train, y_train))
        print("scores test")
        print(model.score(x_test, y_test))
        y_pred = model.predict(x_test)
        print(classification_report(y_test, y_pred))
        return self.save_model(model)

    def save_model(self, model):
        # Save the model
        fake_news_model = open(os.path.normpath(
            os.getcwd() + os.sep)+'\model\classification.model', 'wb')
        pickle.dump(model, fake_news_model)
        fake_news_model.close()
        print("classification model saved!")

    def load_model(self, result):
        # load the model
        with open(os.path.normpath(os.getcwd() + os.sep)+'\model\classification.model', 'rb') as f:
            pclass = pickle.load(f)
            final_outcome = pclass.predict(result)[0]
            return final_outcome

