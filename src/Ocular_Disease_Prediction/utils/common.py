import os 
from src.Ocular_Disease_Prediction.logging import logger
from pathlib import Path 
import yaml 
from box import ConfigBox
from typing import Any
from ensure import ensure_annotations
from box.exceptions import BoxValueError\


@ensure_annotations
def read_yaml(path_to_yaml : Path) -> ConfigBox :
    '''
        reads the yaml file and returns

        Args:   
            path_to_yaml : takes path like input

        Returns: 
            ConfigBox: ConfigBox Type
    '''
    try:
        with open(path_to_yaml) as f:
            content = yaml.safe_load(f)
            logger.info(f'yaml file {path_to_yaml} was read successfully')
            return ConfigBox(content)
    
    except BoxValueError:
        raise ValueError("yaml file is empty")

    except Exception as e:
        raise e
    
    
@ensure_annotations
def create_directories(path_to_directories : Path , verbose = True):
    '''
        creates the list of directories

        Args:
            path_to_directories: list of the path of the directories
            ignore_log(bool, optional) : ignore if multiple directories is to be created. Default to False
    '''

    for i in path_to_directories:
        os.makedirs(i , exist_ok=True)
        if verbose :
            logger.info(f"Created directory at : {i}")


@ensure_annotations
def get_size(path : Path) -> str:
    '''
        Returns the size of the File

        Args:
            path : Path of the file
        Reutrns: 
            str: size in KB
    '''

    size_in_KB = round(os.path.getsize(path)/1024)
    return f"~{size_in_KB} in KB"