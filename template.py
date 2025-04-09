import os 
from pathlib import Path
import logging 

logging.basicConfig(level = logging.INFO , format = "[%(asctime)s] : %(message)s" )

project_name = "WineQualityPrediction"

list_of_files = [".github/workflows/.gitkeep",
                 f"src/{project_name}/__init__.py",
                 f"src/{project_name}/components/__init__.py",
                 f"src/{project_name}/utils/__init__.py",
                 f"src/{project_name}/utils/common.py",
                 f"src/{project_name}/config/__init__.py",
                 f"src/{project_name}/config/configuration.py",
                 f"src/{project_name}/pipeline/__init__.py",
                 f"src/{project_name}/entity/config_entity.py",
                 f"src/{project_name}/entity/__init__.py",
                 f"src/{project_name}/constants/__init__.py",
                 "config.yml",
                 "params.yml",
                 "schema.yml",
                 "main.py",
                 "Dockerfile",
                 "setup.py",
                 "research/research.ipynb",
                 "templates/index.html"
                 ]

for file in list_of_files:
    filepath = Path(file)
    filedir , filename = os.path.split(filepath)

    # creating directories : filedir

    if filedir != "":
        os.makedirs(filedir , exist_ok=True)
        logging.info(f"Creating directory {filedir} for the file : {filename}")

    # Creating files in the directories 

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"Creating empty file : {filepath}")

    else:
        logging.info(f"{filename} already exists in {filedir}")

