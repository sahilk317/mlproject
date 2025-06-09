import os
import sys
from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
import pandas as pd


@dataclass
class DataIngestionConfig:
    # train_data_path:str = os.path.join('artifacts','train.csv')
    # test_data_path:str = os.path.join('artifacts','test.csv')
    # raw_data_path:str = os.path.join('artifacts','data.csv')

    feature_store_path:str = os.path.join('artifacts','feature_store')
    ingested_data_path:str = os.path.join('artifacts','ingested_data')
    train_data_path:str = os.path.join(ingested_data_path,'train.csv')
    test_data_path:str = os.path.join(ingested_data_path,'test.csv')
    raw_data_path:str = os.path.join(feature_store_path,'data.csv')


class DataIngestion:

    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        logging.info(f"Data Ingestion Config:{self.data_ingestion_config}")

    def initiate_data_ingestion(self):
        try:
            logging.info('Data Ingestion method starts')
            data = pd.read_csv('D:/studentPerformence/src/notebook/data/raw.csv')
            logging.info('reading completed')

            
            os.makedirs(self.data_ingestion_config.feature_store_path, exist_ok=True)
            os.makedirs(self.data_ingestion_config.ingested_data_path, exist_ok=True)

            data.to_csv(self.data_ingestion_config.raw_data_path, index=False, header=True)

            logging.info('train test split initiated')

            train_set , test_set = train_test_split(data,test_size=0.3,random_state=43)

            train_set.to_csv(self.data_ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.data_ingestion_config.test_data_path, index=False, header=True)

            logging.info('Ingestion of data is completed')
            return (
                self.data_ingestion_config.train_data_path,
                self.data_ingestion_config.test_data_path,
                self.data_ingestion_config.raw_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)



    
if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()