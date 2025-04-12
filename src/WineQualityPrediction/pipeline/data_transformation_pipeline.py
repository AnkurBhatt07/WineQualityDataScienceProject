from src.WineQualityPrediction.config.configuration import ConfigurationManager
from src.WineQualityPrediction.components.data_transformation import DataTransformation

class DataTransformationPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.train_test_splitting()


