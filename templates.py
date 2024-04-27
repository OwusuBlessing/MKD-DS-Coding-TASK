import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

project_name = "product_recommender"
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/data_preparation/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/Webscraper/__init__.py",
    f"src/{project_name}/OCR/__init__.py",
    f"src/{project_name}/image_recognition/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb"]

for file_path in list_of_files:
    filepath = Path(file_path)
    filedri, filename = os.path.split(filepath)
    if filedri != "":
        os.makedirs(filedri, exist_ok=True)
        logging.info(f"Creating directory: {filedri} for the file: {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {file_path}")
    else:
        logging.info(f"{filename} already exists")





