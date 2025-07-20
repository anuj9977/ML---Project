import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt
from src.exception import CustomException
from src.logger import logging
import dill 
import os
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=True)

        with open(file_path , 'wb') as f:
            dill.dump(obj,f)

    except Exception as e:
        raise CustomException(e,sys)
    
def evaluate_model(X_train,y_train,X_test,y_test,models,param):
    try:
        report={}
        for i in range(len(list(models))):
            model=list(models.values())[i]
            para=param[list(models.keys())[i]]
            # model.fit(X_train,y_train) ## Train model
            grid_search = GridSearchCV(estimator=model, param_grid=para, cv=5, n_jobs=-1)
            grid_search.fit(X_train,y_train)

            model.set_params(**grid_search.best_params_)
            model.fit(X_train,y_train)
            


            y_train_pred=model.predict(X_train) 
            y_test_pred=model.predict(X_test) ## Predict on test data

            train_model_score=r2_score(y_train,y_train_pred)

            test_model_score=r2_score(y_test,y_test_pred)
            report[list(models.keys())[i]]= test_model_score

        return report

    except Exception as e:
        raise CustomException(e,sys)
    



