import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import html
import array
import ftfy
import emoji
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from string import digits
# from sklearn.naive_bayes import MultinomialNB
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import confusion_matrix


def read_csv():
    df = pd.read_csv(r"E:\gather Dataset\covid_dataset.csv")
    df.loc[df['label'] == 'fake', 'label'] = '0'
    df.loc[df['label'] == 'Fake', 'label'] = '0'
    df.loc[df['label'] == 'FAKE', 'label'] = '0'
    df.loc[df['label'] == 'TRUE', 'label'] = '1'
    no_of_fakes = df.loc[df['label'] == '0'].count()[0]
    no_of_trues = df.loc[df['label'] == '1'].count()[0]
    print(no_of_fakes)
    print(no_of_trues)
    text_column = pd.DataFrame(df,columns=['text'])
    return text_column

def remove_emoji(text):
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U0001F1E6-\U0001F1FF"  # flags
        u"\U0001F1F2-\U0001F1F4"  # Macau flag
        u"\U0001F600-\U0001F64F"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U0001F1F4"
        u"\U0001F1F2"
        u"\U0001F620"
        u"\u200d"
        u"\u2640-\u2642"
        "]+", flags=re.UNICODE)
    emoji_removed_text = emoji_pattern.sub(r'', text)
    return emoji_removed_text


cleaned_data = []
def clean(text_list):
    for text in text_list:
        remove_emoji_text = remove_emoji(text) #remove emoji
        remove_url= re.sub(r"http\S+", " ", remove_emoji_text) #remove url
        remove_amp=html.unescape(remove_url) #remove amp
        remove_html_tags = re.sub(r'<[^>]*>', '', remove_amp) # remove html
        remove_expression=re.sub(r"[^a-zA-Z0-9]+", ' ', remove_html_tags)
        remove_numbers = re.sub(r"(^|\W)\d+",'', remove_expression)
        remove_num_String = re.sub(r'\d+', '', remove_numbers)
        remove_aetm = ftfy.fix_text(remove_num_String) #remove aetm
        final_data=remove_aetm.lower() 
        junk_free_sentence = re.sub("[^\w\s]", " ", final_data) # Remove non-letters, but don't remove whitespaces just yet
        if junk_free_sentence not in cleaned_data:
            cleaned_data.append(junk_free_sentence)
    return cleaned_data

token_list = []
def tokenize_text(text_list):
    for text in text_list:
        tokens = word_tokenize(text)
        for token in tokens:
            if token not in token_list:
                token_list.append(token)
    return token_list

lemmatized_sentence=[]
def lemmatization(text_list):
    for text in text_list:
        word_list = word_tokenize(text)
        lemmatizer = WordNetLemmatizer() 
        lemmatized_output = ' '.join([lemmatizer.lemmatize(w) for w in word_list])
        if lemmatized_output not in lemmatized_sentence:
            lemmatized_sentence.append(lemmatized_output)
    return lemmatized_sentence  

def tfidf_text(text):
    text_data = np.array(text)
    tfidf = TfidfVectorizer(min_df=0.1,lowercase=True, preprocessor=None, stop_words='english', use_idf=True,norm='l2',smooth_idf=True)
    feature_matrix = tfidf.fit_transform(text_data)
    feature_matrix.toarray()
    tfidf.get_feature_names() 
    return pd.DataFrame(feature_matrix.toarray(), columns=tfidf.get_feature_names())
        
my_list=[]
def pre_process_text():
    text_column = read_csv()
    for index, row in text_column.iterrows():
        if row['text'] not in my_list:
            my_list.append(row['text'])
    cleaned = clean(my_list)
    lemmatized = lemmatization(cleaned)
    return lemmatized

cleaned_text = pre_process_text()
# tfidf_text(cleaned_text)
print(tfidf_text(cleaned_text))
