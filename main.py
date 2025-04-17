# # Testing the logger 

# from src.WineQualityPrediction import logger 
# logger.info("welcome to the custom logging")
# logger.info("Cheecking the logging process")

from src.WineQualityPrediction import logger
from src.WineQualityPrediction.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.WineQualityPrediction.pipeline.data_validation_pipeline import DataValidationPipeline
from src.WineQualityPrediction.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.WineQualityPrediction.pipeline.model_trainer_pipeline import ModelTrainerPipeline
from src.WineQualityPrediction.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline
if __name__ == "__main__":
    try :
        Stage_name = "Data Ingestion Stage"
        logger.info(f">>>>> stage {Stage_name} started")
        obj = DataIngestionPipeline()
        obj.initiate_data_ingestion()
        logger.info(f">>>>> stage {Stage_name} completed <<<<< ")

        Stage_name = "Data Validation Stage"
        logger.info(f">>>>> stage {Stage_name} started")
        obj = DataValidationPipeline()
        obj.run_data_validation_pipeline()
        logger.info(f">>>>> stage {Stage_name} completed <<<<< ")

        Stage_name = "Data Transformation Stage"
        logger.info(f">>>>> stage {Stage_name} started")
        obj = DataTransformationPipeline()
        obj.initiate_data_transformation()
        logger.info(f">>>>> stage {Stage_name} completed <<<<< ")

        Stage_name = "Model Training Stage"
        logger.info(f">>>>> stage {Stage_name} started")
        obj = ModelTrainerPipeline()
        obj.initiate_model_training()
        logger.info(f">>>>> stage {Stage_name} completed <<<<< ")

        Stage_name = "Model Evaluation Stage"
        logger.info(f">>>>> stage {Stage_name} started <<<<<")
        obj = ModelEvaluationPipeline()
        obj.initiate_model_evaluation_pipeline()
        logger.info(f">>>>> stage {Stage_name} completed <<<<<")


    except Exception as e:
        logger.exception(e)
        raise e
