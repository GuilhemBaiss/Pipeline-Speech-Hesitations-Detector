#@Author : Guilhem Baissus
#Algorithm written during an internship at Laboratoire d'ingénierie Cognitive Sémantique (Lincs) located in Montreal, Quebec
#My internship was supervised by Sylvie Ratté

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

class Dataset:

    @staticmethod
    def get_data(path_dataset, test_size = 0.1):
        """
        returns xtrain, xtest, xvalidation, ytrain, ytest, yvalidation from dataset
        """
        data = pd.read_csv(path_dataset, sep=",")
        predict = "classification"
        X = np.array(data.drop(predict, axis=1))
        y = np.array(data[predict])

        xtrain, xtest, ytrain, ytest = train_test_split(X, y, test_size=test_size)

        return xtrain, xtest, ytrain, ytest




