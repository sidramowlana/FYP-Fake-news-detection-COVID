import access_train_dataset
import pickle
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

class train_model_class:
    def __init__(self):
        pass

    def train_start(self,x):
        x = x
        csv_label = access_train_dataset.access_dataset_class()
        y = csv_label.read_label_csv()
        x_train, x_test, y_train, y_test = train_test_split(x, y, shuffle=True, test_size=0.2, random_state=11)
        model = MultinomialNB()
        model.fit(x_train, y_train)
        print(model.score(x_train, y_train))
        print(model.score(x_test, y_test))
        model.predict(x_test)
        return self.save_model(model)
        # return predictions
        # predictions = model.predict(x_test)
        # cm = confusion_matrix(y_test, predictions)

    def save_model(self,model):
        fake_news_model = open('model_pickle','wb')
        pickle.dump(model,fake_news_model)
        fake_news_model.close()
        print("model saved to file")

    def load_model(self,result):
        with open('model_pickle','rb') as f:
            loaded_model = pickle.load(f)  
            new_d = loaded_model
            print("here")
            print(new_d)
            print("new d predicting")
            print(new_d.predict(result))
            return new_d.predict(result)
            # print("new_result")
            # print(new_d)
            # return new_result