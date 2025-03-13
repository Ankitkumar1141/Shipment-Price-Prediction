from src.Shipment_Price_Prediction.logger import logging
from src.Shipment_Price_Prediction.exception import CustomException
from src.Shipment_Price_Prediction.components.data_ingestion import DataIngestion
from src.Shipment_Price_Prediction.components.data_ingestion import DataIngestionConfig
import sys

if __name__=="__main__":
    logging.info("Execution has started")
    try:
        #data_ingestion_config = DataIngestionConfig()
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()

    except Exception as e:
        raise CustomException(e,sys)
