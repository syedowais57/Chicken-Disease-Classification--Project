import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
import base64
from typing import Union
from pathlib import Path

import logging
logger = logging.getLogger(__name__)

@ensure_annotations
def read_yaml(path_to_yaml: Union[str, Path]) -> ConfigBox:
    """Read YAML file and return its content as ConfigBox."""
    if not path_to_yaml:
        raise ValueError("Path to YAML file cannot be empty")
    
    if isinstance(path_to_yaml, Path):
        path_to_yaml = str(path_to_yaml)
    
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            if content is None:
                raise ValueError("YAML file is empty")
            
            # Debugging output
            print(f"YAML content: {content}")

            return ConfigBox(content)
    except yaml.YAMLError as yaml_error:
        raise ValueError(f"Error parsing YAML file: {yaml_error}")
    except BoxValueError:
        raise ValueError("Error processing YAML file with ConfigBox")
    except Exception as e:
        raise e


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """ Create a list of directories.

    Args:
        path_to_directories (list): List of paths of directories to create.
        verbose (bool, optional): If True, log the creation of directories. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """ Save JSON data to a file.

    Args:
        path (Path): Path to save the JSON file.
        data (dict): Data to be saved in the JSON file.
    """
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
        logger.info(f"JSON file saved: {path} saved successfully")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """ Load JSON data from a file.

    Args:
        path (Path): Path to load the JSON file.

    Returns:
        ConfigBox: Data as ConfigBox object instead of dict.
    """
    with open(path) as f:
        data = json.load(f)
        logger.info(f"JSON file loaded successfully from: {path}")
        return ConfigBox(data)

@ensure_annotations
def save_bin(data: any, path: Path):
    """ Save binary data to a file.

    Args:
        data (Any): Data to be saved in binary format.
        path (Path): Path to save the binary file.
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"Binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> any:
    """ Load binary data from a file.

    Args:
        path (Path): Path to load the binary file.

    Returns:
        Any: Data stored in the file.
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded successfully from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """ Get the size of a file.

    Args:
        path (Path): Path of the file.

    Returns:
        str: Size of the file in KB.
    """
    size_in_kb = round(os.path.getsize(path) / 1024)
    return f"~{size_in_kb} KB"

def decode_image(imgstring: str, file_name: str):
    """ Decode a base64 string and save it as an image file.

    Args:
        imgstring (str): Base64 encoded image string.
        file_name (str): Path to save the decoded image file.
    """
    img_data = base64.b64decode(imgstring)
    with open(file_name, 'wb') as f:
        f.write(img_data)

def encode_image_into_base(cropped_image_path: str) -> str:
    """ Encode an image file to a base64 string.

    Args:
        cropped_image_path (str): Path of the image file to encode.

    Returns:
        str: Base64 encoded image string.
    """
    with open(cropped_image_path, "rb") as f:
        return base64.b64encode(f.read()).decode('utf-8')
