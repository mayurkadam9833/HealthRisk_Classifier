from src.HealthRisk_Classifier.config.configuration import ConfigManager
from src.HealthRisk_Classifier.components.data_transformation import DataTransformation


"""
DataTransformationPipeline class is pipeline to preprocess data 
[drop feartures,fill missing values,encoding,oversampling,scaling,split into tarin & test]
"""
class DataTransformationPipeline: 
    def __init__(self):
        pass 

    def main(self): 
        config=ConfigManager()
        data_transformation_config=config.get_data_transformation_config()
        data_transformation=DataTransformation(config=data_transformation_config)
        data_transformation.drop_features()
        data_transformation.drop_na_rows()
        data_transformation.fill_na_values()
        data_transformation.encode_data()
        data_transformation.sampled_scale_split()