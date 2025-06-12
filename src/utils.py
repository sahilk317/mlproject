import os
import sys
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from src.components.data_ingestion import DataIngestionConfig
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

    except Exception as e:
        raise CustomException(e,sys)
    

    
    