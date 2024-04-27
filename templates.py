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






"JUMBO BAG RED RETROSPOT": "https://www.google.com/search?q=JUMBO+BAG+RED+RETROSPOT&sca_esv=5d5b8bda91a2629d&rlz=1C1KNTJ_enNG1063NG1063&udm=2&biw=1536&bih=738&sxsrf=ACQVn0-iMROXT9_-z_C21DIjQ49iBpHtmQ%3A1714199868453&ei=PJ0sZu-2GvKrhbIPk7uK0AU&ved=0ahUKEwjvxO2R5OGFAxXyVUEAHZOdAloQ4dUDCBA&uact=5&oq=JUMBO+BAG+RED+RETROSPOT&gs_lp=Egxnd3Mtd2l6LXNlcnAiF0pVTUJPIEJBRyBSRUQgUkVUUk9TUE9UMgUQABiABEjxEVDKC1jKC3ABeACQAQCYAfoBoAH6AaoBAzItMbgBA8gBAPgBAvgBAZgCAqACigKYAwCIBgGSBwUxLjAuMaAHUA&sclient=gws-wiz-serp",
  "PARTY BUNTING": "https://www.google.com/search?q=%22PARTY+BUNTING&sca_esv=5d5b8bda91a2629d&rlz=1C1KNTJ_enNG1063NG1063&udm=2&biw=1536&bih=738&sxsrf=ACQVn0-WTHkXcEefuAJL1ALkjgjobRnC3A%3A1714199916138&ei=bJ0sZuKGCKTNhbIPu6qxUA&ved=0ahUKEwji7Myo5OGFAxWkZkEAHTtVDAoQ4dUDCBA&uact=5&oq=%22PARTY+BUNTING&gs_lp=Egxnd3Mtd2l6LXNlcnAiDiJQQVJUWSBCVU5USU5HMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABEi2EFD0Clj0CnABeACQAQCYAd4DoAHeA6oBAzQtMbgBA8gBAPgBAvgBAZgCAqACigSYAwCIBgGSBwUxLjQtMaAH-AQ&sclient=gws-wiz-serp",
  "LUNCH BAG RED RETROSPOT": "https://www.google.com/search?q=LUNCH+BAG+RED+RETROSPOT&sca_esv=5d5b8bda91a2629d&rlz=1C1KNTJ_enNG1063NG1063&udm=2&biw=1536&bih=738&sxsrf=ACQVn0_53HiAcETEpgzkcwL7UYNu7MSjUg%3A1714199947450&ei=i50sZqSEG4eBhbIPhtCu-A8&ved=0ahUKEwjk9cO35OGFAxWHQEEAHQaoC_8Q4dUDCBA&uact=5&oq=LUNCH+BAG+RED+RETROSPOT&gs_lp=Egxnd3Mtd2l6LXNlcnAiF0xVTkNIIEJBRyBSRUQgUkVUUk9TUE9USPsPUJMKWJMKcAF4AJABAJgBmQKgAZkCqgEDMi0xuAEDyAEA-AEC-AEBmAIBoAIXwgIKEAAYgAQYQxiKBcICBRAAGIAEmAMAiAYBkgcBMaAHLQ&sclient=gws-wiz-serp"
}