
import pandas as pd
import numpy as np

class access_dataset_class:
    my_list=[]
    
    def __init__(self):
        pass

    def read_text_csv(self):
        df = pd.read_csv(r"covid_dataset.csv")
        df.loc[df['label'] == 'fake', 'label'] = '0'
        df.loc[df['label'] == 'Fake', 'label'] = '0'
        df.loc[df['label'] == 'FAKE', 'label'] = '0'
        df.loc[df['label'] == 'TRUE', 'label'] = '1'
        df.loc[df['label'] == 'true', 'label'] = '1'
        df.loc[df['label'] == 'True', 'label'] = '1'
        text_column = pd.DataFrame(df,columns=['text'])
        for index, row in text_column.iterrows():
            self.my_list.append(row['text'])
        return self.my_list

    def read_label_csv(self):
        df = pd.read_csv(r"covid_dataset.csv")
        df.loc[df['label'] == 'fake', 'label'] = '0'
        df.loc[df['label'] == 'Fake', 'label'] = '0'
        df.loc[df['label'] == 'FAKE', 'label'] = '0'
        df.loc[df['label'] == 'TRUE', 'label'] = '1'
        df.loc[df['label'] == 'true', 'label'] = '1'
        df.loc[df['label'] == 'True', 'label'] = '1'
        label_column = df['label'].values        
        return label_column   