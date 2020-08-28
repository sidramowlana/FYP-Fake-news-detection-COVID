# class TrainModel:
#     import re
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# import html
# import array
# import ftfy
# import emoji
# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords
# from nltk.stem import WordNetLemmatizer 
# from sklearn.feature_extraction.text import TfidfVectorizer
# from string import digits
# from sklearn.naive_bayes import MultinomialNB
# from sklearn.ensemble import RandomForestClassifier
# from sklearn import svm
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import confusion_matrix


# class Preprocess:    
#     def __init__(self):
#         pass

#     def read_text_csv(self):
#         df = pd.read_csv(r"E:\gather Dataset\covid_dataset.csv")
#         df.loc[df['label'] == 'fake', 'label'] = '0'
#         df.loc[df['label'] == 'Fake', 'label'] = '0'
#         df.loc[df['label'] == 'FAKE', 'label'] = '0'
#         df.loc[df['label'] == 'TRUE', 'label'] = '1'
#         text_column = pd.DataFrame(df,columns=['text'])
#         return text_column

#     def read_label_csv(self):
#         df2 = pd.read_csv(r"E:\gather Dataset\covid_dataset.csv")
#         df2.loc[df2['label'] == 'fake', 'label'] = '0'
#         df2.loc[df2['label'] == 'Fake', 'label'] = '0'
#         df2.loc[df2['label'] == 'FAKE', 'label'] = '0'
#         df2.loc[df2['label'] == 'TRUE', 'label'] = '1'
#         label_column = pd.DataFrame(df2,columns=['label'])
#         return label_column    

#     def remove_emoji(self,text):
#         emoji_pattern = re.compile("["
#             u"\U0001F600-\U0001F64F"  # emoticons
#             u"\U0001F300-\U0001F5FF"  # symbols & pictographs
#             u"\U0001F680-\U0001F6FF"  # transport & map symbols
#             u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
#             u"\U0001F1E6-\U0001F1FF"  # flags
#             u"\U0001F1F2-\U0001F1F4"  # Macau flag
#             u"\U0001F600-\U0001F64F"
#             u"\U00002702-\U000027B0"
#             u"\U000024C2-\U0001F251"
#             u"\U0001f926-\U0001f937"
#             u"\U0001F1F4"
#             u"\U0001F1F2"
#             u"\U0001F620"
#             u"\u200d"
#             u"\u2640-\u2642"
#             "]+", flags=re.UNICODE)
#         emoji_removed_text = emoji_pattern.sub(r'', text)
#         return emoji_removed_text


#     def clean(self,text_list):
#         cleaned_data = []
#         for text in text_list:
#             remove_emoji_text = self.remove_emoji(text) #remove emoji
#             remove_url= re.sub(r"http\S+", " ", remove_emoji_text) #remove url
#             remove_amp=html.unescape(remove_url) #remove amp
#             remove_html_tags = re.sub(r'<[^>]*>', '', remove_amp) # remove html
#             remove_expression=re.sub(r"[^a-zA-Z0-9]+", ' ', remove_html_tags)
#             remove_numbers = re.sub(r"(^|\W)\d+",'', remove_expression)
#             remove_num_String = re.sub(r'\d+', '', remove_numbers)
#             remove_aetm = ftfy.fix_text(remove_num_String) #remove aetm
#             final_data=remove_aetm.lower() 
#             junk_free_sentence = re.sub("[^\w\s]", " ", final_data) # Remove non-letters, but don't remove whitespaces just yet
#             cleaned_data.append(junk_free_sentence)
#         return cleaned_data

    
#     def tokenize_text(self,text_list):
#         token_list = []
#         for text in text_list:
#             tokens = word_tokenize(text)
#             for token in tokens:
#                 if token not in token_list:
#                     token_list.append(token)
#         return token_list

    
#     def lemmatization(self,text_list):
#         lemmatized_sentence=[]
#         for text in text_list:
#             word_list = word_tokenize(text)
#             lemmatizer = WordNetLemmatizer() 
#             lemmatized_output = ' '.join([lemmatizer.lemmatize(w) for w in word_list])
#             lemmatized_sentence.append(lemmatized_output)
#         return lemmatized_sentence  
  
    
#     def pre_process_text(self):
#         my_list=[]
#         text_column = self.read_text_csv()
#         for index, row in text_column.iterrows():
#             my_list.append(row['text'])
#         cleaned = self.clean(my_list)
#         lemmatized = self.lemmatization(cleaned)
#         return lemmatized

   

#     # cleaned_text = self.pre_process_text()
#     # x = tfidf_text(cleaned_text)
#     # text_label = read_label_csv()
#     # y = text_label
#     # # FYP Preprocess_featureextract - upyter filename

#     # def train_model():
#     #     x_train, x_test, y_train, y_test = train_test_split(x, y, shuffle=True, test_size=0.2, random_state=11)
#     #     model = MultinomialNB()
#     #     model.fit(x_train, y_train)
#     #     print(model.score(x_train, y_train))
#     #     print(model.score(x_test, y_test))

#     # train_model()