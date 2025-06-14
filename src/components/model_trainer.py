import sys
import os 
from src.logger import logging
from src.exception import CustomException
from dataclasses import dataclass

from sklearn.metrics import r2_score
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import (
    AdaBoostRegressor,
    RandomForestRegressor,
    GradientBoostingRegressor
)

# from xgboost import XGBRegressor
# from catboost import CatBoostRegressor

from src.utils import save_object,evaluate_model


@dataclass
class ModelTrainerConfig :
    trained_model_file_path = os.path.join('artifacts','model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self,train_array,test_array,preprocessor_path):

        try:

            x_train,y_train,x_test,y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )

            models = {
                'Linear Regression' : LinearRegression(),
                'Adaboost Regressor':AdaBoostRegressor(),
                'RandomForesr Regressor': RandomForestRegressor(),
                'GradientBoosting Regressor': GradientBoostingRegressor(),
                'K-neighbor Regressor': KNeighborsClassifier(),
            }

            model_report : dict = evaluate_model(x_train,x_test,y_train,y_test,models)

            best_model_score = max(model_report.values())

            best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]

            best_model = models[best_model_name]

            save_object(
                self.model_trainer_config.trained_model_file_path,
                best_model
            )

            prediction = best_model.predict(x_test)

            r2 = r2_score(y_test,prediction)

            return r2 , model_report



        except Exception as e:
            raise CustomException(e,sys)
        



    