
from src.WineQualityPrediction.config.configuration import ConfigurationManager
from src.WineQualityPrediction.components.data_validation import DataValidation

class DataValidationPipeline:
    def __init__(self):
        pass
    def run_data_validation_pipeline(self):
        try :
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(config = data_validation_config)
            validation_status = data_validation.get_data_validation_status()
            print(f"Validation Status : {validation_status}")

        except Exception as e :
            raise e