# This will be put in src/WineQualityPrediction/config/configuration.py
from src.WineQualityPrediction.constants import config_file_path , params_file_path , schema_file_path
from src.WineQualityPrediction.utils.common import read_yaml , create_directories
from src.WineQualityPrediction.entity.config_entity import DataIngestionConfig , DataValidationConfig , DataTransformationConfig , ModelTrainerConfig

class ConfigurationManager:
    def __init__(self , config_file_path = config_file_path ,
                 params_file_path = params_file_path ,
                   schema_file_path = schema_file_path):
        
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)
        self.schema = read_yaml(schema_file_path)

        create_directories([self.config.artifacts_root])

    
    def get_data_ingestion_config(self) -> DataIngestionConfig :
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        data_ingestion_config = DataIngestionConfig(
            root_dir= config.root_dir,
            source_url= config.source_url,
            local_data_file=config.datafileLocation,
            unzip_dir= config.unzip_dir

        )
        return data_ingestion_config
    


    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS
        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            DataToValidateLoc=config.dataset_location,
            StatusFileFolder=config.root_dir,
            StatusFileName=config.status_file,
            AllSchema=schema
        )
        return data_validation_config
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation
        create_directories([config.root_dir])
        data_transformation_config = DataTransformationConfig(root_dir= config.root_dir ,
                                                              data_path=config.data_path)
        
        return data_transformation_config
    
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_training
        params = self.params.ElasticNet 
        target_column = self.schema.TARGET_COLUMN.name
        create_directories([config.root_dir])
        model_trainer_config = ModelTrainerConfig(root_dir=config.root_dir ,
                                                  train_data_path=config.train_data_path ,
                                                  test_data_path= config.test_data_path ,
                                                  model_name=config.model_name ,
                                                  alpha=params.alpha,
                                                  l1_ratio=params.l1_ratio,
                                                  target_column=target_column)
        
        return model_trainer_config
    


