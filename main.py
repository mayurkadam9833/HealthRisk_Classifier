from src.HealthRisk_Classifier.logging import logger
from src.HealthRisk_Classifier.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.HealthRisk_Classifier.pipeline.data_validation_pipeline import DataValidationPipeline


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