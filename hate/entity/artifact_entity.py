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

# Data Transformation Related Artifact
@dataclass
class DataTransformationArtifacts:
    transformed_data_path: str


