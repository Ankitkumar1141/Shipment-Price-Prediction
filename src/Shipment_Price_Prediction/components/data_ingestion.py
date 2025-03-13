import os
import sys
from src.Shipment_Price_Prediction.exception import CustomException
from src.Shipment_Price_Prediction.logger import logging
import pandas as pd


from src.Shipment_Price_Prediction.utils import read_sql_data
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifact', 'train.csv')
    test_data_path: str = os.path.join('artifact', 'test.csv')
    raw_data_path: str = os.path.join('artifact', 'raw.csv')

class DataIngestion:
    def __init__(self):  # Fix: Changed `_init_` to `__init__`
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            logging.info("Reading data from MySQL database...")

            df = read_sql_data()  # Fetch data from MySQL

            if df.empty:
                raise Exception("Dataframe is empty. Check MySQL table or query.")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            print(f"Saving raw data to: {self.ingestion_config.raw_data_path}")
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            print(f"Total rows in dataset: {df.shape[0]}")

            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            print(f"Train set size: {train_set.shape}")
            print(f"Test set size: {test_set.shape}")

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Data Ingestion is completed")

            return self.ingestion_config.train_data_path, self.ingestion_config.test_data_path

        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()
    logging.info("Data ingestion successfully done")
