from src.HealthRisk_Classifier.config.configuration import ConfigManager
from src.HealthRisk_Classifier.components.model_evaluation import ModelEvaluation


"""
ModelEvaluationPipeline class is pipeline to evaluate model on 
test data and save metrics as json file at defined path
"""
class ModelEvaluationPipeline: 
    def __init__(self):
        pass

    def main(self): 
        config=ConfigManager()                                            # create object of configmanager
        model_evaluation_config=config.get_model_evaluation_config()      # get model evaluation config
        model_evaluation=ModelEvaluation(config=model_evaluation_config)  # create object of ModelEvaluation
        model_evaluation.evaluate_model()                                 # method for evaluate model on test data and save json file