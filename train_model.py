from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import access_train_dataset

class train_model_class:
    def __init__(self):
        pass

    def train_start(self,x):
        x = x
        csv_label = access_train_dataset.access_dataset_class()
        y = csv_label.read_label_csv()
        # y = access_train_dataset.access_dataset.read_label_csv()
        x_train, x_test, y_train, y_test = train_test_split(x, y, shuffle=True, test_size=0.2, random_state=11)
        return x_train
    #     model = MultinomialNB()
    #     model.fit(x_train, y_train)
    #     print(model.score(x_train, y_train))
    #     print(model.score(x_test, y_test))