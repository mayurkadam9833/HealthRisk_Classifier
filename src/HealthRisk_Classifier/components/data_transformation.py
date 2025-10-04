import os
import joblib
import pandas as pd 
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from sklearn.preprocessing import StandardScaler
from src.HealthRisk_Classifier.entity.config_entity import DataTransformationConfig
from src.HealthRisk_Classifier.logging import logger


"""DataTransformation class contain method that preprocess data(drop irrelavent columns),fill missing values,drop missing rows
 encode categorical data,oversampling,scale,split data into train an test"""
class DataTransformation:
    def __init__(self,config:DataTransformationConfig):
        self.config=config 
        self.sample=SMOTE()
        self.scale=StandardScaler()
    
    # method to drop irrelvent columns
    def drop_features(self): 
        data=pd.read_csv(self.config.data_file)
        data.drop(["Gender","random_notes"],axis=1,inplace=True)
        return data 
    
    # method to drop missing rows in target column
    def drop_na_rows(self): 
        data=self.drop_features()
        data.dropna(subset=[self.config.target_col],inplace=True)
        return data 
    
    # method to fill null values
    def fill_na_values(self): 
        data=self.drop_na_rows()
        for col in data[["Age","Glucose","Blood Pressure"]]: 
            mean=data[col].mean()
            data[col].fillna(mean,inplace=True)
        return data 
    
    # method to encode data
    def encode_data(self): 
        data=self.fill_na_values()
        data[self.config.target_col]=data[self.config.target_col].replace({
                                                                    "Hypertension":0,
                                                                    "Diabetes":1,
                                                                    "Obesity":2,
                                                                    "Healthy":3,
                                                                    "Asthma":4,
                                                                    "Arthritis":5,
                                                                    "Cancer":6})
        return data
    
    # method to oversampling, scaling, split into train and test
    def sampled_scale_split(self): 
        data=self.encode_data()

        # divide input and target columns
        x=data.drop([self.config.target_col],axis=1)
        y=data[self.config.target_col]

        # split train and test data
        train_x,test_x,train_y,test_y=train_test_split(x,y,test_size=0.2,random_state=42)

        # oversampling for data imbalanced
        sample_train_x,sample_train_y=self.sample.fit_resample(train_x,train_y)

        #scaling data
        scale_train_x=self.scale.fit_transform(sample_train_x)
        scale_test_x=self.scale.transform(test_x)

        # concat target and input columns
        train=pd.concat([pd.DataFrame(scale_train_x).reset_index(drop=True),sample_train_y.reset_index(drop=True)],axis=1)
        test=pd.concat([pd.DataFrame(scale_test_x).reset_index(drop=True),pd.Series(test_y).reset_index(drop=True)],axis=1)
        
        # saved train and test data at defined path
        train.to_csv(os.path.join(self.config.root_dir,"train.csv"),index=False)
        test.to_csv(os.path.join(self.config.root_dir,"test.csv"),index=False)

        logger.info(train.shape)
        logger.info(test.shape)

         
        


    