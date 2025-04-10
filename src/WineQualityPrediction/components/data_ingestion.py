import zipfile 
import urllib.request as request 
import os 
from src.WineQualityPrediction import logger 
from src.WineQualityPrediction.entity.config_entity import DataIngestionConfig




class DataIngestion:
    def __init__(self , config : DataIngestionConfig):
        self.config = config 
    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename , headers = request.urlretrieve(url = self.config.source_url ,
                                                     filename = self.config.local_data_file)
            logger.info(f"{filename} downloaded with following info : \n {headers}")

        else :
            logger.info(f"File already exists")

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        with zipfile.ZipFile(self.config.local_data_file , 'r') as file:
            file.extractall(unzip_path)
        logger.info(f"{self.config.local_data_file} extracted at {unzip_path}")