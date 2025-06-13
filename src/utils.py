import os
import sys
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from src.components.data_ingestion import DataIngestionConfig
from sklearn.metrics import r2_score
import dill 



def dtypes_of_features():
    data_ingestion_config = DataIngestionConfig()
    data_path = data_ingestion_config.raw_data_path
    df = pd.read_csv(data_path)
    cols = df.columns
    num_features = [col for col in cols if df[col].dtype == 'int']
    cat_features = [col for col in cols if df[col].dtype == 'O']

    return num_features , cat_features


def save_object(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,'wb') as f:
            dill.dump(obj,f)

            # dill.dump is used to convert python object into binary format and save it into f file object

    except Exception as e:
        raise CustomException(e,sys)
    

def evaluate_model(x_train,x_test,y_train,y_test,models):
    report = {}
    try:

        for i in range(len(list(models))):

            model = list(models.values())[i]
            model.fit(x_train,y_train)
            y_train_pred = model.predict(x_train)
            y_test_pred = model.predict(x_train)

            train_model_score = r2_score(y_train,y_train_pred)

            test_model_score = r2_score(y_test,y_test_pred)

            report[list(models.keys())[i]] = train_model_score

        return report

        
    except Exception as e:
        raise CustomException(e,sys)

    

    
    