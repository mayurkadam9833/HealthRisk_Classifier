import os
import joblib
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from src.HealthRisk_Classifier.entity.config_entity import ModelTrainerConfig
from src.HealthRisk_Classifier.logging import logger



"""ModelTrainer class contain method of train_model
which train model with train dataset and save train model to defined path"""
class ModelTrainer: 
    def __init__(self,config:ModelTrainerConfig):
        self.config=config 
        self.model=GradientBoostingClassifier(learning_rate=self.config.learning_rate,n_estimators=self.config.n_estimators,max_depth=self.config.max_depth,min_samples_split=self.config.min_samples_split,min_samples_leaf=self.config.min_samples_leaf)

    # method to train model
    def model_trainer(self): 
        # read train data
        data=pd.read_csv(self.config.train_data_path)

        # split into input and target column
        train_x=data.drop([self.config.target_col],axis=1)
        train_y=data[self.config.target_col]

        # train model
        model=self.model.fit(train_x,train_y)

        # save model at defined path
        model_path=os.path.join(self.config.root_dir,"model.joblib")

        joblib.dump(model,model_path)

        logger.info("model trained and save sucessfully")


