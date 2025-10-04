from src.HealthRisk_Classifier.logging import logger
from src.HealthRisk_Classifier.pipeline.data_ingestion_pipeline import DataIngestionPipeline

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
