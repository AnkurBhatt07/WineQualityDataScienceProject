from dataclasses import dataclass 
from pathlib import Path 

@dataclass 
class DataIngestionConfig:
    root_dir : Path 
    source_url : str 
    local_data_file : Path 
    unzip_dir : Path 

@dataclass
class DataValidationConfig:
    StatusFileFolder : Path
    DataToValidateLoc : Path 
    StatusFileName : Path 
    AllSchema : dict

@dataclass
class DataTransformationConfig:
    root_dir : Path 
    data_path : Path 
    
@dataclass
class ModelTrainerConfig:
    root_dir : Path 
    train_data_path : Path
    test_data_path : Path
    model_name : str
    alpha : float
    l1_ratio : float
    target_column:str


@dataclass
class ModelEvaluationConfig:
    root_dir : Path 
    test_data_path : Path
    model_path : Path 
    metric_file_name : Path 
    all_params : dict 
    target_column : Path 
    mlflow_uri : str 


