import os
import logging 
from pathlib import Path  

# configure logging 
logging.basicConfig(level=logging.INFO,format="[%(asctime)s : %(message)s]")

# assign project name
project_name="HealthRisk_Classifier"

# list of file and their directories required for project
list_of_files=[
    f"src/{project_name}/__init__.py", 
    f"src/{project_name}/components/__init__.py", 
    f"src/{project_name}/utils/__init__.py", 
    f"src/{project_name}/utils/common.py", 
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py", 
    f"src/{project_name}/config/configuration.py", 
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml", 
    "schema.yaml", 
    "main.py", 
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

# create a loop to create file and file directories if they are not already exists
for filepath in list_of_files: 
    filepath=Path(filepath)
    file_dir,file_name=os.path.split(filepath)   # split file dir and file

    # create file directory if not already exists
    if file_dir != "": 
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f"create {file_dir} for {file_name}")
    
    # create a empty file if not already exists
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0): 
        with open(filepath,"w")as file: 
            pass 
        logging.info(f"create empty {file_name} at {filepath}")
    
    # if file already exists this log will return
    else: 
        logging.info(f"{file_name} is alreday exists")
    