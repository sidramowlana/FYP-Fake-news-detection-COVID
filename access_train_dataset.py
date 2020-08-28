
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
        text_column = pd.DataFrame(df,columns=['text'])
        for index, row in text_column.iterrows():
            self.my_list.append(row['text'])
        return self.my_list

    def read_label_csv(self):
        df2 = pd.read_csv(r"covid_dataset.csv")
        df2.loc[df2['label'] == 'fake', 'label'] = '0'
        df2.loc[df2['label'] == 'Fake', 'label'] = '0'
        df2.loc[df2['label'] == 'FAKE', 'label'] = '0'
        df2.loc[df2['label'] == 'TRUE', 'label'] = '1'
        label_column = pd.DataFrame(df2,columns=['label'])
        return label_column   
    

