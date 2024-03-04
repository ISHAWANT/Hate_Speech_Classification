from dataclasses import dataclass

@dataclass
class DataIngestionArtifacts:
    """
    Represents the artifacts generated during the data ingestion process.

    Attributes:
        imbalance_data_file_path (str): The file path to the imbalance data.
        raw_data_file_path (str): The file path to the raw data.
    """

    def __init__(self, imbalance_data_file_path: str, raw_data_file_path: str):
        """
        Initializes the DataIngestionArtifacts object.

        Args:
            imbalance_data_file_path (str): The file path to the imbalance data.
            raw_data_file_path (str): The file path to the raw data.
        """
        self.imbalance_data_file_path = imbalance_data_file_path
        self.raw_data_file_path = raw_data_file_path

# Data Transformation 
@dataclass
class DataTransformationArtifacts:
    transformed_data_path: str

# Model Training 

@dataclass
class ModelTrainerArtifacts: 
    trained_model_path:str
    x_test_path: list
    y_test_path: list

# Model evaluation artifacts
@dataclass
class ModelEvaluationArtifacts:
    is_model_accepted: bool  

