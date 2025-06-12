from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.exception import CustomException
import sys


if __name__ == "__main__":
    transformer = DataTransformation()
    transformer.initiate_data_transformation(
        train_path="D:/studentPerformence/artifacts/ingested_data/test.csv",
        test_path="D:/studentPerformence/artifacts/ingested_data/test.csv"
    )


