#@Author : Guilhem Baissus
#Algorithm written during an internship at Laboratoire d'ingénierie Cognitive Sémantique (Lincs) located in Montreal, Quebec
#My internship was supervised by Sylvie Ratté

import sys
import os
from extracting_features.extract_features import *
from returning_predictions.predict import *
from functions.login import *
from train_models_new_dataset.create_dataset_and_train import *

#-----------------------------------------------------------------------------------------------------------
#DEFAULT HYPERPARAMETERS 
MINIMUM_SILENCE_DURATION = 0.1
SIZE_FRAME = 0.5
SIZE_BETWEEN_FRAMES = 0.1
NUMBER_OF_ENERGY_POINTS = 100
NUMBER_OF_STABILITY_DISTANCES = 10

#DEFAULT PATHS
PATH_SOUND_FILES = os.path.join(os.getcwd(), "audios")
PATH_CSV_FEATURES_FILES = os.path.join(os.getcwd(), "csv-features")
PATH_CSV_RESULTS_FILES = os.path.join(os.getcwd(), "csv-results")
PATH_DATASET = os.path.join(os.getcwd(), "dataset")
PATH_TO_MODELS = os.path.join(os.getcwd(), "src", "trained_models")
PATH_CSV_FEATURES_ANNOTATED = os.path.join(os.getcwd(), "csv-features-annotated")

#MODEL USED BY DEFAULT
MODEL_NAME = "decision_tree_model"

#MODELS

MODELS_LIST = ["decision_tree_model", "random_forest_model", "svm_model"]
#TASK
"""1 = get predictions, 2 = get only features, 3 = train models with new dataset """
TASK = 1

#-----------------------------------------------------------------------------------------------------------

TASK,MINIMUM_SILENCE_DURATION, SIZE_FRAME, SIZE_BETWEEN_FRAMES, NUMBER_OF_ENERGY_POINTS, NUMBER_OF_STABILITY_DISTANCES, PATH_SOUND_FILES, PATH_CSV_FEATURES_FILES, PATH_CSV_RESULTS_FILES, MODEL_NAME, PATH_DATASET, PATH_TO_MODELS, PATH_CSV_FEATURES_ANNOTATED = login(TASK, MINIMUM_SILENCE_DURATION, SIZE_FRAME, SIZE_BETWEEN_FRAMES, NUMBER_OF_ENERGY_POINTS, NUMBER_OF_STABILITY_DISTANCES, PATH_SOUND_FILES, PATH_CSV_FEATURES_FILES, PATH_CSV_RESULTS_FILES, MODEL_NAME, PATH_DATASET, PATH_TO_MODELS, PATH_CSV_FEATURES_ANNOTATED)

#-----------------------------------------------------------------------------------------------------------
#Get features
if TASK == 1 or TASK ==2:
    number_audios_processed = mainExtractFeatures(PATH_SOUND_FILES, PATH_CSV_FEATURES_FILES, MINIMUM_SILENCE_DURATION, SIZE_FRAME, SIZE_BETWEEN_FRAMES, NUMBER_OF_ENERGY_POINTS, NUMBER_OF_STABILITY_DISTANCES)

    if number_audios_processed ==0:
        print("The folder given in argument does not contain any sound file \n")
        sys.exit()
    else:
        print("Features were extracted successfully\n")

#-----------------------------------------------------------------------------------------------------------
#Get predictions
if TASK ==1:
    number_csv_processed = mainPredict(PATH_CSV_FEATURES_FILES, PATH_CSV_RESULTS_FILES, MODEL_NAME)

    if number_csv_processed ==0:
        print("The folder given in argument does not contain any csv file containing features \n")
    else:
        print("Results successfully added \n")

#-----------------------------------------------------------------------------------------------------------
#Train models with new dataset
elif TASK ==3:
    #DEFAULT PATHS
    DATASET_NAME = "dataset"

    not_valid_answer7 = True
    while(not_valid_answer7):
        print("The current name of the new dataset is : {}".format(DATASET_NAME))
        print("options : \n")
        print(" \t [1] : change name of dataset")
        print(" \t [2] : create dataset")
        print(" \t [3] : train a model")
        print(" \t [4] : train all models")
        print(" \t [5] : done")
        print("(1/2/3/4/5) ? ")
        answer7 = input()

        #Change paths or name of dataset
        if "1" in answer7 and len(answer7) <2:
            print("enter name for the dataset :")
            DATASET_NAME = input()
        elif "2" in answer7 and len(answer7) <2:
            mainCreateDataset(PATH_CSV_FEATURES_ANNOTATED, PATH_DATASET, DATASET_NAME)
            print("'{}' was created with success \n".format(DATASET_NAME))
        #Train a model
        elif "3" in answer7 and len(answer7) <2:
            print("The following trained models are present :")
            for models in MODELS_LIST:
                print("\t - {}".format(models))
            print("Which model do you want to train ?")
            model_found = False
            answer9 = input()
            for models in MODELS_LIST:
                if models in answer9:
                    model_found = True
                    path_to_dataset = os.path.join(PATH_DATASET, DATASET_NAME + ".csv")
                    mainTrainModels(path_to_dataset, PATH_TO_MODELS, models)
            if model_found == False:
                print("the model was not found, try again")

        elif "4" in answer7 and len(answer7) <2:
            for models in MODELS_LIST:
                print("training {} ...".format(models))
                path_to_dataset = os.path.join(PATH_DATASET, DATASET_NAME + ".csv")
                mainTrainModels(path_to_dataset, PATH_TO_MODELS, models)
        elif "5" in answer7 and len(answer7) <2:
            not_valid_answer7 = False
        else:
            print("{} is not an option".format(answer7))


