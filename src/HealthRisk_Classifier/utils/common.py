import os 
import yaml
import json 
from pathlib import Path 
from box import ConfigBox
from ensure import ensure_annotations
from box.exceptions import BoxValueError
from src.HealthRisk_Classifier.logging import logger

# Function to read yaml file
@ensure_annotations 
def read_yaml(path_to_yaml:Path)-> ConfigBox: 
    try: 
        with open(path_to_yaml,"r")as yaml_file: 
            content=yaml.safe_load(yaml_file)
            logger.info(f"yaml file loaded sucessfully from {path_to_yaml}")
    
    except BoxValueError:
        raise ValueError("yaml file empty")
    
    except Exception as e :
        raise e

    return ConfigBox(content)

# Function for creating new directories
@ensure_annotations 
def create_dir(file_path:list,verbose=True): 
    for path in file_path: 
        os.makedirs(path,exist_ok=True)
        if verbose: 
            logger.info(f"directory create sucessfully")


# Function to get size of file
@ensure_annotations 
def get_size(file): 
    size_in_kb=round(os.path.getsize(file)/1024)
    return f"file size : {size_in_kb}KB"


# function to save dict to json file
@ensure_annotations 
def save_json(path:Path,data:dict):
    with open(path,"w")as file: 
        json.dump(data,file,indent=4) 
        logger.info(f"json file saved sucessfully")
