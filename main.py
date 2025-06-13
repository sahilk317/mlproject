from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.exception import CustomException
import sys
from src.components.model_trainer import ModelTrainer,ModelTrainerConfig


if __name__ == "__main__":
    transformer = DataTransformation()
    train_arr , test_arr, path = transformer.initiate_data_transformation(
        train_path="D:/studentPerformence/artifacts/ingested_data/test.csv",
        test_path="D:/studentPerformence/artifacts/ingested_data/test.csv"
    )

    obj = ModelTrainer()
    r2 = obj.initiate_model_trainer(train_arr,test_arr,path)
    print(r2)




