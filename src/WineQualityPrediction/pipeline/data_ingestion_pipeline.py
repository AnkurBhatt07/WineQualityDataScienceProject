from src.WineQualityPrediction.config.configuration import ConfigurationManager
from src.WineQualityPrediction.components.data_ingestion import DataIngestion
from src.WineQualityPrediction import logger 

Stage_name = "Data Ingestion State"

class DataIngestionPipeline:
    def __init__(self) :
        pass 
    
    def initiate_data_ingestion(self):
        config = ConfigurationManager()
        dataIngestionconfig = config.get_data_ingestion_config()
        dataIngestion = DataIngestion(config = dataIngestionconfig)
        dataIngestion.download_file()
        dataIngestion.extract_zip_file()


