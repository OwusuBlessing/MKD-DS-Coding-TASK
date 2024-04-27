import os
from box.exceptions import  BoxValueError
import yaml
from src.product_recommender.logging import  logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import shutil
import os
import re


@ensure_annotations
def read_yaml(path_to_yaml) -> ConfigBox:
    """
    reads yaml file and returns
    Args:
       Valueerror: IF YAML file is empty
       e: empty file

    Raises:
    ConfigBox.ConfigBox:
    """
    try:
        with open(path_to_yaml, "r") as f:
            config = yaml.safe_load(f)
            return ConfigBox(config)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        logger.error(e)



@ensure_annotations
def create_directory(path_to_directories:list,verbose=True):
    """create list of directories
    Args:

        path_to_directories(list):list of directories
        ignore_log(bool,optiolnal): ignore if multiple dirs is to be created
    """
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"Directory {path} created")

@ensure_annotations

def get_size(path:Path) -> str:
    """
    get size of a file
    Args:
        path(Path): path to file
    Returns:
        size(str): size of file
    """
    size_kb = round(os.path.getsize(path)/1024)
    return  f"~{size_kb} KB"


def save_filecsv(df,location,file_name): 
    if not os.path.exists(location):
            os.makedirs(location)

    file_name = "cleaned_data.csv"
    path = os.path.join(location, file_name)
    df.to_csv(path)



def remove_non_numeric(text):
    return re.sub(r'[^\d.]+', '', text)