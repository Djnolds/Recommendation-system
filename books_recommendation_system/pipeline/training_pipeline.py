from books_recommendation_system.components.stage_00_data_ingestion import DataIngestion
from books_recommendation_system.components.stage_01_data_validation import DataValidation
from books_recommendation_system.components.stage_02_data_transformation import DataTransformation
from books_recommendation_system.components.stage_03_model_trainer import ModelTrainer


class TrainingPipeline:
    def __init__(self):
        self.data_ingestion = DataIngestion()
        self.data_validation = DataValidation()
        self.data_transformation = DataTransformation()
        self.model_trainer = ModelTrainer()

    def start_training_pipeline(self):
        """
        Starts the training pipeline
        :return: none
        """
        self.data_ingestion.initiate_data_ingestion()
        
        # The data validation is initiated after the data ingestion
        self.data_validation.initiate_data_validation()
        
        # The data transformation is initiated after the data validation
        self.data_transformation.initiate_data_transformation()
        
        # The model trainer is initiated after the data transformation
        self.model_trainer.initiate_model_trainer() 