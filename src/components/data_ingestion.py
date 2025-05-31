import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

@dataclass
class data_ingestionconfig:
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")
    raw_data_path: str = os.path.join("artifacts", "data.csv")

class data_ingestion:
    def __init__(self):
        self.ingestion = data_ingestionconfig()

    def data_ingestion_initiate(self):
        logging.info("data ingestion initiated")
        try:
            df = pd.read_csv("notebook\data\stud.csv")
            train_set,test_set = train_test_split(df, test_size=0.2, random_state=42)
            logging.info("train test split happend succesfully")

            os.makedirs(os.path.dirname(self.ingestion.train_data_path), exist_ok=True)
            logging.info("directory created sucesfully")

            df.to_csv(self.ingestion.raw_data_path, index=False,header=True)
            train_set.to_csv(self.ingestion.train_data_path, index=False,header=True)
            test_set.to_csv(self.ingestion.test_data_path, index=False,header=True)
            logging.info("files saved succesfully")

            return(
                self.ingestion.train_data_path,
                self.ingestion.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)


if __name__ == "__main__":
    obj=data_ingestion()
    train_data,test_data = obj.data_ingestion_initiate()



        