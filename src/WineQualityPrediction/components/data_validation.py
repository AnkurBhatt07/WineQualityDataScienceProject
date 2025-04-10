from src.WineQualityPrediction.constants import schema_file_path
from src.WineQualityPrediction.utils.common import read_yaml , create_directories
from src.WineQualityPrediction.entity.config_entity import DataValidationConfig
import pandas as pd

schema = read_yaml(schema_file_path)
schema_cols = schema.COLUMNS.keys()
schema_cols_dtype = list(schema.COLUMNS.values())
class DataValidation:
    def __init__(self , config : DataValidationConfig) :
        self.config = config 

    def get_data_validation_status(self):
        try :
            validation_status = None
            data = self.config.DataToValidateLoc
            data = pd.read_csv(data)
            data_columns = list(data.columns)
            dtypes_list = [col.name for col in list(data.dtypes)]
            
            for i,col in enumerate(data_columns):
                if col not in schema_cols:
                    validation_status = False
                    with open(self.config.StatusFileName , 'w') as file:
                        file.write(f"Validation Status : {validation_status}")
                    break
                if dtypes_list[i] != schema_cols_dtype[i]:
                    validation_status = False
                    with open(self.config.StatusFileName , 'w') as file:
                        file.write(f"Validation Status : {validation_status}")
                    break

            if validation_status == None:
                validation_status = True
                with open(self.config.StatusFileName , 'w') as file:
                        file.write(f"Validation Status : {validation_status}")

            

            return validation_status
        
        except Exception as e:
            raise e
        
        
    
            
        