from dataclasses import dataclass 
from pathlib import Path 

"""DataIngestionConfig class will return directories for download data,zip data,extract data path and 
source url for data ingestion process """
@dataclass(frozen=True)
class DataIngestionConfig: 
    root_dir: Path 
    source_url: str 
    local_data_file: Path 
    unzip_dir: Path

"""DataValidationConfig class will return
dataset path,data validation folder,target column, all_columns from schema 
for data validation process """
@dataclass(frozen=True)
class DataValidationConfig: 
    root_dir: Path 
    unzip_data_path: Path 
    validation: str
    all_schema: dict

"""DataTransformationConfig class will return
data transformation folder path,dataset path,target column for data transformation"""
@dataclass(frozen=True)
class DataTransformationConfig: 
    root_dir: Path
    data_file: Path
    target_col: str 

"""ModelTrainerConfig class will return
model trainer folder path,traindata path,target column,model path,parameters for model trainer"""
@dataclass(frozen=True)
class ModelTrainerConfig: 
    root_dir:Path                 
    train_data_path: Path
    model_name: str 
    learning_rate: float
    n_estimators: int
    max_depth: int
    min_samples_split: int
    min_samples_leaf: int 
    target_col: str


"""ModelEvaluationConfig class will return
model Evaluation folder path,testdata path,target column,model path for model Evaluation"""
@dataclass(frozen=True)
class ModelEvaluationConfig: 
    root_dir: Path 
    test_data_path: Path
    model_path: Path 
    evaluation: str
    target_col: str