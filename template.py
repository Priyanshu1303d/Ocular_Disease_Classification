import os 
import logging
from pathlib import Path


logging.basicConfig(level = logging.INFO , format = '[%(asctime)s]: %(message)s')

project_name = 'Ocular_Disease_Prediction'

list_of_files = [
    './github/workflows/.gitkeep',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/constants/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/__init__.py'
    'dvc.yaml',
    'params.yaml',
    'setup.py',
    'requirements.txt',
    'config/config.yaml',
    'research/trials.ipynb'
]

for i in list_of_files:
    filepath = Path(i)

    filedir , filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok = True)
        logging.info(f"Created the filedir : {filedir} with file name : {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath , 'w') as f:
            pass
            logging.info(f"Created the empty file : {filepath}")

    else:
        logging.info(f"{filepath} File Already Exists")