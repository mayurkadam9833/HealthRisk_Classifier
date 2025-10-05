import os 
import joblib 
import pandas as pd 
from pathlib import Path
from sklearn.metrics import accuracy_score,confusion_matrix,precision_score,recall_score,f1_score
from src.HealthRisk_Classifier.entity.config_entity import ModelEvaluationConfig 
from src.HealthRisk_Classifier.utils.common import save_json



"""ModelEvaluation class contain method of evaluation in which it will 
return evaluation metrics for classification """
class ModelEvaluation: 
    def __init__(self,config:ModelEvaluationConfig):
        self.config=config 
        self.model=joblib.load(self.config.model_path)

    # method to get metrics for classification
    def get_metrics(self,actual,predicted): 
        acc=accuracy_score(actual,predicted)
        cf=confusion_matrix(actual,predicted)
        pr=precision_score(actual,predicted,average='weighted')
        rc=recall_score(actual,predicted,average='weighted')
        f1=f1_score(actual,predicted,average='weighted')
        return acc,cf,pr,rc,f1

    # method to evaluate model on test data and save metrics score
    def evaluate_model(self): 
        try:
            # read test data
            data=pd.read_csv(self.config.test_data_path)

            # split data into input and target column
            test_x=data.drop([self.config.target_col],axis=1)
            test_y=data[self.config.target_col]

            # make prediction on test data
            pred=self.model.predict(test_x)

            # get metrics score for test data
            acc,cf,pr,rc,f1=self.get_metrics(test_y,pred)

            # create dict of metrics
            metrics={"accuracy score":acc,"confusion matrix":cf.tolist(),"precision score":pr,"recall score":rc,"f1 score":f1}

            # save metrics as json file to defined path
            save_json(Path(self.config.evaluation),metrics)

        except Exception as e: 
            raise e


                