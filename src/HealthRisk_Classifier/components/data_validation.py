import pandas as pd
from src.HealthRisk_Classifier.entity.config_entity import DataValidationConfig
from src.HealthRisk_Classifier.logging import logger 


"""
DataValidation class contain method for 
check and validation of schema of dataset with defined schema
"""
class DataValidation: 
    def __init__(self,config:DataValidationConfig):
        self.config=config

    # method to check if dataset columns match schema columns
    def schema_validation(self): 
        try: 
            schema_val=True  
            data=pd.read_csv(self.config.unzip_data_path)    # read dataset
            all_cols=list(data.columns)                      # get dataset column names
            all_schema=self.config.all_schema.keys()         # schema column names

            # loop through dataset columns and check against schema
            for col in all_cols:
                if col == "Medical Condition": 
                    continue 
                if col not in all_schema:
                    schema_val=False 
                
                with open(self.config.validation,"w")as file: 
                    file.write(f"schema validation:{schema_val}")
            
            logger.info(f"schema validation completed")

        except Exception as e: 
            raise e    
            
                

            