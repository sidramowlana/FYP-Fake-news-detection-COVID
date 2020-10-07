import re
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
import nltk
nltk.download('punkt')


class pre_process_class:
    def __init__(self):
        pass

    def remove_emoji(self, text):
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

    def clean(self, text_list):
        cleaned_data = []
        for text in text_list:
            data = self.remove_emoji(text)  # remove emoji
            data = re.sub(r"http\S+", " ", data)  # remove url
            data = html.unescape(data)  # remove amp
            data = re.sub(r'<[^>]*>', '', data)  # remove html
            data = re.sub(r"[^a-zA-Z0-9]+", ' ', data)  # Remove unwanted chars
            data = re.sub(r"(^|\W)\d+", '', data)  # Remove numbers
            # Remove unwanted charaters with numbers
            data = re.sub(r'\d+', '', data)
            data = ftfy.fix_text(data)  # remove aetm
            data = data.lower()  # lower case
            # Remove non-letters, but don't remove whitespaces just yet
            data = re.sub(r"[^\w\s]", " ", data)
            data = re.sub(r' +', ' ', data)  # remove multiple white space
            data = self.tokenize(data)
            cleaned_data.append(data)
        return cleaned_data

    def tokenize(self, text):
        stop_words = set(stopwords.words('english'))
        word_tokens = word_tokenize(text)
        filtered_sentence = []
        for word_token in word_tokens:
            if word_token not in stop_words:
                filtered_sentence.append(word_token)
        # Joining words
        text = (' '.join(filtered_sentence))
        return text

    def lemmatization(self, text_list):
        lemmatized_sentence = []
        for text in text_list:
            word_list = word_tokenize(text)
            lemmatizer = WordNetLemmatizer()
            lemmatized_output = ' '.join(
                [lemmatizer.lemmatize(w) for w in word_list])
            lemmatized_sentence.append(lemmatized_output)
        return lemmatized_sentence

    def pre_process_text(self, text):
        cleaned = self.clean(text)
        lemmatized = self.lemmatization(cleaned)
        return lemmatized
