import joblib
import pandas as pd 
from pathlib import Path





class Prediction_pipeline: 
    def __init__(self):
        self.model=joblib.load(Path("artifacts/model_trainer/model.joblib"))
        self.scale=joblib.load(Path("artifacts/data_transformation/scale.joblib"))
        self.encode=joblib.load(Path("artifacts/data_transformation/encode.joblib"))

    def preprocess(self,data:pd.DataFrame): 
        data=self.scale.transform(data)
        return data 
    
    def prediction(self,data:pd.DataFrame): 
        processed_data=self.preprocess(data)
        preds=self.model.predict(processed_data)
        decoded = self.encode.inverse_transform(preds)
        return decoded

