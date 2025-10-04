from src.HealthRisk_Classifier.config.configuration import ConfigManager
from src.HealthRisk_Classifier.components.data_validation import DataValidation


"""
DataValidationPipeline class is pipeline to validation of dataset schema
"""
class DataValidationPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigManager()
        data_validation_config=config.get_data_validation_config()
        data_validation=DataValidation(config=data_validation_config)
        data_validation.schema_validation()