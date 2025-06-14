import sys
import os
from src.logger import logging
from src.exception import CustomException
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer


class TrainingPipeline:
    def __init__(self):
        pass

    def run_training_pipeline(self):
        try:
            logging.info('Starting Data Ingestion')
            data_ingestion =  DataIngestion()
            training_path , testing_path = data_ingestion.initiate_data_ingestion()
            logging.info(f'Train path and Test path : {training_path},{testing_path}')

            logging.info('Starting Data Transformation')
            data_transformation = DataTransformation()
            train_array , test_array , preprocessor_path = data_transformation.initiate_data_transformation(training_path,testing_path)
            logging.info(f'Data Transformation Completed')

            logging.info('Model Training Started')
            model_trainer = ModelTrainer()
            best_r2_score , model_report = model_trainer.initiate_model_trainer(train_array,test_array)
            logging.info(f'Model Training Completed and best r2 score is {best_r2_score},model report is {model_report}')



        except Exception as e:
            raise CustomException(e,sys)