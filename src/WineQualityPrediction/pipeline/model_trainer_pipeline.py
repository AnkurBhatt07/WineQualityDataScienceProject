from src.WineQualityPrediction.config.configuration import ConfigurationManager
from src.WineQualityPrediction.components.model_trainer import ModelTrainer
class ModelTrainerPipeline:
    def __init__(self ):
        pass

    def initiate_model_training(self):
        try :
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer = ModelTrainer(config=model_trainer_config)
            model_trainer.initiate_model_training()

        except Exception as e:
            raise e 
        
        