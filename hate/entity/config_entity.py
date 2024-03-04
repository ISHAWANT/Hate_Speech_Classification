from dataclasses import dataclass
import os
from hate.constants import * 

@dataclass
class DataIngestionConfig:
    """
    Configuration class for data ingestion.

    Attributes:
        BUCKET_NAME (str): The name of the bucket where data is stored.
        ZIP_FILE_NAME (str): The name of the zip file containing the data.
        DATA_INGESTION_ARTIFACTS_DIR (str): Directory for storing data ingestion artifacts.
        DATA_ARTIFACTS_DIR (str): Directory for storing data artifacts.
        NEW_DATA_ARTIFACTS_DIR (str): Directory for storing new data artifacts.
        ZIP_FILE_DIR (str): Directory for the zip file.
        ZIP_FILE_PATH (str): Full path to the zip file.
    """

    def __init__(self):
        # Setting default values for attributes
        self.BUCKET_NAME:str = BUCKET_NAME
        self.ZIP_FILE_NAME: str = ZIP_FILE_NAME

        # Constructing directory paths based on current working directory and constants
        self.DATA_INGESTION_ARTIFACTS_DIR: str = os.path.join(os.getcwd(), ARTIFACTS_DIR, DATA_INGESTION_ARTIFACTS_DIR)
        self.DATA_ARTIFACTS_DIR: str = os.path.join(self.DATA_INGESTION_ARTIFACTS_DIR, DATA_INGESTION_IMBALANCE_DATA_DIR)
        self.NEW_DATA_ARTIFACTS_DIR: str = os.path.join(self.DATA_INGESTION_ARTIFACTS_DIR, DATA_INGESTION_RAW_DATA_DIR)
        self.ZIP_FILE_DIR = os.path.join(self.DATA_INGESTION_ARTIFACTS_DIR)
        self.ZIP_FILE_PATH = os.path.join(self.DATA_INGESTION_ARTIFACTS_DIR, self.ZIP_FILE_NAME)

# Data Transformation Realted Config 
@dataclass
class DataTransformationConfig:
    def __init__(self):
        self.DATA_TRANSFORMATION_ARTIFACTS_DIR: str = os.path.join(os.getcwd(),ARTIFACTS_DIR,DATA_TRANSFORMATION_ARTIFACTS_DIR)
        self.TRANSFORMED_FILE_PATH = os.path.join(self.DATA_TRANSFORMATION_ARTIFACTS_DIR,TRANSFORMED_FILE_NAME)
        self.ID = ID
        self.AXIS = AXIS
        self.INPLACE = INPLACE 
        self.DROP_COLUMNS = DROP_COLUMNS
        self.CLASS = CLASS 
        self.LABEL = LABEL
        self.TWEET = TWEET
