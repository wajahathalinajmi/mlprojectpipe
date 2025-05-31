import os
import sys
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.impute import SimpleImputer
from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass
from src.utils import save_dill_object

@dataclass
class datatransformationconfig:
    preprocessor_obj_file: str = os.path.join("artifacts", "preprocessor.pkl")

class data_transformation:
    def __init__(self):
        self.tranformation = datatransformationconfig()

    def get_data_transform(self):
        try:
             numerical_columns = ["writing_score", "reading_score"]
             categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",]
             
             num_pipeline = Pipeline(
                 steps=[
                     ("simple imputer",SimpleImputer(strategy='median')),
                     ("scaler", StandardScaler(with_mean=False))
                 ]
             )

             cat_pipeline = Pipeline(
                 steps=[
                     ("simple imputer",SimpleImputer(strategy='most_frequent')),
                     ("encoder", OneHotEncoder()),
                     ("scaler", StandardScaler(with_mean=False))
                 ]
             )
            
             logging.info(f"cat columns are {categorical_columns}")
             logging.info(f"num columns are {numerical_columns}")

             preprocessor = ColumnTransformer([
                 ("numerical pipeline", num_pipeline, numerical_columns),
                 ("cat pipeline", cat_pipeline, categorical_columns)

             ])

             return preprocessor
   
        except Exception as e :
            raise CustomException(e,sys)
        
    def initiate_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("train test read succesfully")

            logging.info("initiating preprocessor object call")

            preprocessor_obj = self.get_data_transform()

            target_column = 'math_score'
            feature_train_df = train_df.drop(columns=[target_column], axis=1)
            target_train_df = train_df[target_column]

            feature_test_df = test_df.drop(columns=[target_column], axis=1)
            target_test_df = test_df[target_column]

            logging.info("applying preprocessing on train and test ")

            feature_train_df_arr = preprocessor_obj.fit_transform(feature_train_df)
            feature_test_df_arr = preprocessor_obj.transform(feature_test_df)

            logging.info("completed preprocessing succesfully")

            train_arr = np.c_[feature_train_df_arr, np.array(target_train_df)]
            test_arr = np.c_[feature_test_df_arr, np.array(target_test_df)]

            logging.info("saving preprocessor obj file")

            save_dill_object(
                 file_path = self.tranformation.preprocessor_obj_file,
                 obj = preprocessor_obj
            )

           
            return(
                train_arr,
                test_arr,
                self.tranformation.preprocessor_obj_file
            )
        
        except Exception as e:
            raise CustomException(e,sys)