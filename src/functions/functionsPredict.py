#@Author : Guilhem Baissus
#Algorithm written during an internship at Laboratoire d'ingénierie Cognitive Sémantique (Lincs) located in Montreal, Quebec
#My internship was supervised by Sylvie Ratté

import pandas as pd
import numpy as np
import pickle
import os
from sklearn.model_selection import train_test_split


def get_x(path_csv_file):
    """
    returns xtrain, xtest, xvalidation, ytrain, ytest, yvalidation from dataset
    """
    data = pd.read_csv(path_csv_file, sep=",")
    drop_data_columns = ["classification", "start_time", "end_time"]
    data = data.drop(drop_data_columns, axis =1)
    X = np.array(data)

    return X

def load_model(model_name):
    path = os.path.join(os.getcwd(), "src", "trained_models", "{}.pickle".format(model_name))
    pickle_in = open(path, "rb")
    model = pickle.load(pickle_in)
    return model

def get_predictions(model, path_csv_file):

    X = get_x(path_csv_file)
    y = model.predict(X)
    return y

def create_csv(path_csv_file, path_csv_results_file, y):
    """
    créer dictionnaire avec valeurs : classification, start_time, end_time
    ouvrir features_csv
    prendre column start_time end_time et mettre dans csv créé
    prendre résultats prédictions et mettre dans classification
    créer csv avec dictionnaire
    mettre dans csv_results
    """
    
    data = pd.read_csv(path_csv_file, sep=",")
    start_time = np.array(data["start_time"])
    end_time = np.array(data["end_time"])

    data_columns = {
        "classification" : y,
        "start_time": start_time,
        "end_time" : end_time
    }

    df = pd.DataFrame()
    df = pd.DataFrame(data_columns,columns=list(data_columns.keys()))
    df.to_csv(path_csv_results_file, index = False)










