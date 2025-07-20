import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt
from src.exception import CustomException
from src.logger import logging
import dill 
import os
def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=True)

        with open(file_path , 'wb') as f:
            dill.dump(obj,f)

    except Exception as e:
        raise CustomException(e,sys)