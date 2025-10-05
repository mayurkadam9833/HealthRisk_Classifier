from src.HealthRisk_Classifier.logging import logger
from src.HealthRisk_Classifier.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.HealthRisk_Classifier.pipeline.data_validation_pipeline import DataValidationPipeline
from src.HealthRisk_Classifier.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.HealthRisk_Classifier.pipeline.model_trainer_pipeline import ModelTrainerPipeline

# data ingestion pipeline execution
stage_one="Data Ingestion"
if __name__ == "__main__": 
    try:
        logger.info(f"<<<< stage: {stage_one} started")
        obj=DataIngestionPipeline()
        obj.main()
        logger.info(f"<<<< stage: {stage_one} completed")
    
    except Exception as e: 
        logger.info(e)
        raise e

# data validation pipeline execution
stage_two="Data Validation"
if __name__=="__main__": 
    try: 
        logger.info(f"<<<< stage: {stage_two} started")
        obj=DataValidationPipeline()
        obj.main()
        logger.info(f"<<<< stage: {stage_two} completed")
    
    except Exception as e: 
        logger.info(e)
        raise e


# data transformation pipeline execution
stage_three="Data Transformation"
if __name__=="__main__": 
    try: 
        logger.info(f"<<<< stage: {stage_three} started")
        obj=DataTransformationPipeline()
        obj.main()
        logger.info(f"<<<< stage: {stage_three} completed")
    
    except Exception as e: 
        logger.info(e)
        raise e
    
# Model trainer pipeline execution
stage_four="Model Trainer"
if __name__=="__main__": 
    try: 
        logger.info(f"<<<< stage: {stage_four} started")
        obj=ModelTrainerPipeline()
        obj.main()
        logger.info(f"<<<< stage: {stage_four} completed")
    
    except Exception as e: 
        logger.info(e)
        raise e