import pandas as pd
import wget
import os
import requests
from zipfile import ZipFile

# PATHS
base_path = [YOUR_PROJECT_PATH_HERE]
source_url = "https://assets.datacamp.com/production/repositories/5899/datasets/66691278303f789ca4acd3c6406baa5fc6adaf28/PPR-ALL.zip"
source_path = f"{base_path}/data/source/downloaded_at=2022-03-01/ppr-all.zip"
data_dir = f"{base_path}/raw_data"


# Create a directory at the `path` passed as an argument
def create_directory_if_not_exists(path):
    """
    Create my new data directory (to store ZipFiles)
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)


# Write the file obtained to the specified directory
def download_snapshot():
    """
    Download the desired CSV from the Zip file to a specific folder
    """
    create_directory_if_not_exists(source_path)
    # Open the .zip file in binary mode
    with open(source_path, "wb") as source_ppr:
        response = requests.get(source_url, verify=False)
        source_ppr.write(response.content)


# Download the new dataset
download_snapshot()

# Create my personal data directory - for CSVs only
os.makedirs(os.path.dirname(data_dir), exist_ok=True)

# Extract the correct CSV into my personal data folder
with ZipFile(source_path, 'r') as zip:
    filenames = zip.namelist()
    result = zip.extract(filenames[0], data_dir)
    
    
def extract_data():
    df = pd.read_csv('[YOUR_PROJECT_PATH]/data/source/downloaded_at=2022-03-01/ppr-all.zip',
                     encoding='unicode_escape')
    return df
