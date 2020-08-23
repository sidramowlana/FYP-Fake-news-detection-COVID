import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import html
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
    df = pd.read_csv(r"E:\gather Dataset\Book1.csv")
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
        u"\U0001F1F2-\U0001F1F4"  # Macau flag
        u"\U0001F1E6-\U0001F1FF"  # flags
        u"\U0001F600-\U0001F64F"
        u"\U00002702-\U000027B0"
        u"\U000024C2-\U0001F251"
        u"\U0001f926-\U0001f937"
        u"\U0001F1F2"
        u"\U0001F1F4"
        u"\U0001F620"
        u"\u200d"
        u"\u2640-\u2642"
        "]+", flags=re.UNICODE)
    emoji_removed_text = emoji_pattern.sub(r'', text)
    return emoji_removed_text;


def clean(text):
    remove_emoji_text = remove_emoji(text) #remove emoji
    remove_url= re.sub(r"http\S+", "", remove_emoji_text) #remove url
    remove_amp=html.unescape(remove_url) #remove amp
    remove_html_tags = re.sub(r'<[^>]*>', '', remove_amp) # remove html
    remove_expression=re.sub(r"[^a-zA-Z0-9]+", ' ', remove_html_tags)
    remove_numbers = re.sub('[^a-zA-Z]',' ',remove_expression)
    remove_aetm = ftfy.fix_text(remove_numbers) #remove aetm
    cleaned_data=remove_aetm.lower() 
    return cleaned_data

stop_words = set(stopwords.words('english'))
def noise_removal_text(text):
    word_tokens = word_tokenize(text)
    filtered_sentence = []
    for word_token in word_tokens:
        if word_token not in stop_words:
            filtered_sentence.append(word_token)
    join_text = (' '.join(filtered_sentence))
    return join_text

token_list = []
def tokenize_text(text):
    tokens = word_tokenize(text)
    for token in tokens:
        token_list.append(token)
    return token_list

lemmatized_sentence=[]
def lemmatization(text_list):
    lemmatizer = WordNetLemmatizer() 
    for word in text_list:
        lemmatized_text = lemmatizer.lemmatize(word)
        lemmatized_sentence.append(lemmatized_text)
    return lemmatized_sentence;   


list=[]
def tfidf_text(text):
#     vectorizer = TfidfVectorizer(ngram_range=(1,1))
#     vector =  vectorizer.fit_transform(text) 
    tfidf = TfidfVectorizer(strip_accents=None,
                        lowercase=False,
                        preprocessor=None,
                        use_idf=True,
                        norm='l2',
                        smooth_idf=True)
    x = tfidf.fit_transform(text)     
    y = x.todense()
    return x

x_tokens = []
my_list=[]
def pre_process_text():
    text_column = read_csv()
    for row in text_column.iterrows():
        data = row['text']
        cleaned = clean(data)       
        noiseless_text = noise_removal_text(cleaned)
        tokenized = tokenize_text(noiseless_text)
    lemmatized = lemmatization(tokenized)
    print(lemmatized)
    return lemmatized

lemmatization_text = pre_process_text()
tfidf_text(lemmatization_text)