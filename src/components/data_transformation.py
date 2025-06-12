import sys 
import os
import pandas as pd
import numpy as np
from src.exception import CustomException
from src.logger import logging
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler 
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline , make_pipeline
from dataclasses import dataclass
from src.utils import dtypes_of_features
# from src.components.data_ingestion import DataIngestionConfig
from src.utils import save_object




@dataclass
class DataTransformationConfig:
    preprocessor_file_path = os.path.join('artifacts','preprocessor.pkl')


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
        # self.data_ingestion_config = DataIngestionConfig()

    
    def get_data_transformation_obj(self):
        try:
            
            numerical_columns , categorical_columns = dtypes_of_features()

            num_pipeline = Pipeline([
                ('imputer',SimpleImputer(strategy='median')),
                ('scaler',StandardScaler())
            ])

            logging.info('numerical pipeline created')

            cat_pipeline = Pipeline([
                ('imputer',SimpleImputer(strategy='most_frequent')),
                ('encoder',OneHotEncoder()),
                ('scaler',StandardScaler(with_mean=False))
            ])


            logging.info('categorical pipeline created')

            preprocessor = ColumnTransformer([
                ('num_pipeline',num_pipeline,numerical_columns),
                ('cat_pipeline',cat_pipeline,categorical_columns)
            ],remainder='passthrough')

            logging.info('here we are returning preprocessor')

            return preprocessor


        except Exception as e:
            raise CustomException(e,sys)






    def initiate_data_transformation(self,train_path,test_path):

        try:
            train_data = pd.read_csv(train_path)
            test_data = pd.read_csv(test_path)

            logging.info('read train and test data completed')

            preprocessor = self.get_data_transformation_obj()


            target_column_name = 'math_score'

            input_feature_train_df = train_data.drop(columns = [target_column_name])
            output_feature_train_df = train_data[target_column_name]

            input_feature_test_df = test_data.drop(columns = [target_column_name])
            output_feature_test_df = test_data[target_column_name]


            logging.info('applying preprocessing object to train and test data')

            input_feature_train_array = preprocessor.fit_transform(input_feature_train_df)
            input_feature_test_array = preprocessor.transform(input_feature_test_df)

            logging.info('data transformed successfully')

            train_arr = np.c_[
                input_feature_train_array , np.array(output_feature_train_df)
            ]

            test_array = np.c_[
                input_feature_test_array,np.array(output_feature_test_df)
            ]
            logging.info('train and test array created')

            save_object(
                file_path = self.data_transformation_config.preprocessor_file_path,
                obj = preprocessor
            )

            logging.info('save object fun run successfully')

            return (
                train_arr,
                test_array,
                self.data_transformation_config.preprocessor_file_path
            )
        
        except Exception as e:
            raise CustomException(e,sys)
        

