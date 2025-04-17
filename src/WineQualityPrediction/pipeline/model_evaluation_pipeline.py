from src.WineQualityPrediction.config.configuration import ConfigurationManager
from src.WineQualityPrediction.components.model_evaluation import ModelEvaluation


class ModelEvaluationPipeline:

    def __init__(self):
        pass
    def initiate_model_evaluation_pipeline(self):
        try :
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation = ModelEvaluation(config = model_evaluation_config)
            model_evaluation.log_into_mlflow()
        except Exception as e:
            raise e
