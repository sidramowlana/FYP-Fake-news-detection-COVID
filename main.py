import pre_process
import feature_extraction
import access_train_dataset
import train_model

class Main:
    # new text
    text = ['South Australian COVID-19 update 29/8/20. For more information go to https://buff.ly/2IBPz2x or contact the South Australian COVID-19 Information Line on 1800 253 787.']

    # dataset for training
    # text = access_train_dataset.access_dataset_class().read_text_csv()   

    if __name__ == "__main__":
        print("Initializing the main method!")
        processed = pre_process.pre_process_class(text)
        final_text = processed.pre_process_text(text)
        extracted = feature_extraction.feature_extraction_class(final_text)
        result = extracted.tfidf_text(final_text)
        train = train_model.train_model_class()
        print(result)
        # train the model and save
        # trained_result = train.train_start(result)

        # load the modal and runa new text
        train.load_model(result)





































        #   print("Initializing the main method!")
        # # df['new_text'] = df['text']
        # # processed = pre_process.pre_process_class()
        # # df['new_text'] = df['new_text'].apply(processed.pre_process_text)
        # # extracted = feature_extraction.feature_extraction_class()
        # # result = extracted.tfidf_text(df['new_text'])
        # # train = train_model.train_model_class()
        # # print(result)
        # # trained_result = train.train_start(result)
        # print("********************************1********************************")        
        # processed = pre_process.pre_process_class()
        # text = processed.pre_process_text(text)
        # extracted = feature_extraction.feature_extraction_class()
        # result = extracted.tfidf_text(text)
        # print(result)
        # train = train_model.train_model_class()
        # # print(result)
        # model = train.load_model()
        # model.predict(result)

