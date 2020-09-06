import access_train_dataset
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
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score 
from sklearn.model_selection import cross_val_score

class train_model_class:
    def __init__(self):
        pass

    def train_start_Voting_Classifier(self,x):
        x = x
        csv_label = access_train_dataset.access_dataset_class()
        y = csv_label.read_label_csv()      
        x_train, x_test, y_train, y_test = train_test_split(x, y, shuffle=True, test_size=0.2, random_state=11)        
        naive_bayes_model = MultinomialNB()
        svm_model = svm.SVC()
        voting_model = VotingClassifier(
            estimators=[
                ('nb', naive_bayes_model), ('svm', svm_model)],voting='soft')
        voting_model = voting_model.fit(x_train, y_train)        
        # Showign an error
        y_pred = voting_model._predict(x_test) 
        score = accuracy_score(y_test, y_pred.round(), normalize=False) 
        return print("Soft Voting Score % d" % score)        
        # for clf, label in zip([naive_bayes_model, svm_model, voting_model], ['Naive Bayes', 'SVM', 'Ensemble']):
        #     scores = cross_val_score(clf, x_test, y_test, scoring='accuracy', cv=5)
        #     return print("Accuracy: %0.2f (+/- %0.2f) [%s]" % (scores.mean(), scores.std(), label))


    def train_start_NB(self,x):
        x = x
        csv_label = access_train_dataset.access_dataset_class()
        y = csv_label.read_label_csv()      
        x_train, x_test, y_train, y_test = train_test_split(x, y, shuffle=True, test_size=0.2, random_state=11)        

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


    def train_start_RF(self,x):
        x = x
        csv_label = access_train_dataset.access_dataset_class()
        y = csv_label.read_label_csv()
        x_train, x_test, y_train, y_test = train_test_split(x, y, shuffle=True, test_size=0.2, random_state=11)
        model = RandomForestClassifier()
        model.fit(x_train, y_train)
        print("scores train")
        print(model.score(x_train, y_train))
        print("scores test")
        print(model.score(x_test, y_test))
        model.predict(x_test)
        return self.save_model(model)


    def train_start_SVM(self,x):
        x = x
        csv_label = access_train_dataset.access_dataset_class()
        y = csv_label.read_label_csv()
        x_train, x_test, y_train, y_test = train_test_split(x, y, shuffle=True, test_size=0.2, random_state=11)
        model = svm.SVC(kernel='linear') 
        model.fit(x_train, y_train)
        print("scores train")
        print(model.score(x_train, y_train))
        print("scores test")
        print(model.score(x_test, y_test))
        model.predict(x_test)
        return self.save_model(model)


    def train_start_KNN(self,x):
        x = x
        csv_label = access_train_dataset.access_dataset_class()
        y = csv_label.read_label_csv()
        x_train, x_test, y_train, y_test = train_test_split(x, y, shuffle=True, test_size=0.2, random_state=11)
        # Create KNN classifier
        model = KNeighborsClassifier(n_neighbors = 3)
        # Fit the classifier to the data
        model.fit(x_train,y_train)
        print("scores train")
        print(model.score(x_train, y_train))
        print("scores test")
        print(model.score(x_test, y_test))
        model.predict(x_test)
        return self.save_model(model)

    def save_model(self,model):
        fake_news_model = open('nb_model_pickle','wb')
        pickle.dump(model,fake_news_model)
        fake_news_model.close()
        print("model saved to file")

    def load_model(self,result):
        with open('nb_model_pickle','rb') as f:
            loaded_model = pickle.load(f)  
            new_d = loaded_model           
            return new_d.predict(result)




# malmut 