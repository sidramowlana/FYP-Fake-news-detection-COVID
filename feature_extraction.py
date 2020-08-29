import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords

class feature_extraction_class:
    def __init__(self,text):
        self.text = text
    
    stop_words = set(stopwords.words('english'))
    def tfidf_text(self,text):
        text_data = np.array(text)
        tfidf = TfidfVectorizer(min_df=0.1,lowercase=True, preprocessor=None, stop_words='english', use_idf=True,norm='l2',smooth_idf=True)
        feature_matrix = tfidf.fit_transform(text_data)
        feature_matrix_array = feature_matrix.toarray()        
        print(pd.DataFrame(feature_matrix.toarray(), columns=tfidf.get_feature_names()))
        return feature_matrix_array  


















# class feature_extraction_class:
#     def __init__(self):
#         pass

#     stop_words = set(stopwords.words('english'))
#     def tfidf_text(self,text):    
#         # tfidf = TfidfVectorizer(min_df=0.1,lowercase=True, preprocessor=None, stop_words='english', use_idf=True,norm='l2',smooth_idf=True)
#         tfidf = TfidfVectorizer()
#         print(text)
#         feature_matrix = tfidf.fit_transform([text])           
#         # feature_matrix = tfidf.fit_transform(text.values)           
#         feature_matrix_array = feature_matrix.toarray()        
#         return feature_matrix_array