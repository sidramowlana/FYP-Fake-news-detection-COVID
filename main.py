import pre_process
import feature_extraction
import access_train_dataset
import train_model

class Main:
    new_text = "The Corona #virus is a man made studying created in the lab? on 2019-12-12"
    text = access_train_dataset.access_dataset_class().read_text_csv()
    def __init__(self):
        pass

    if __name__ == "__main__":
        print("Initializing the main method!")
        processed = pre_process.pre_process_class(text)
        final_text = processed.pre_process_text(text)
        extracted = feature_extraction.feature_extraction_class(final_text)
        result = extracted.tfidf_text(final_text)
        train = train_model.train_model_class()
        trained_result = train.train_start(result)

        print(trained_result)

    

