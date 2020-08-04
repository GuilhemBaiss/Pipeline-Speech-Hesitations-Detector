#@Author : Guilhem Baissus
#Algorithm written during an internship at Laboratoire d'ingénierie Cognitive Sémantique (Lincs) located in Montreal, Quebec
#My internship was supervised by Sylvie Ratté

import sys
import os
from extracting_features.extractFeatures import *
from returning_predictions.predict import *
from functions.login import *

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
MODEL_NAME = "decision_tree_model"

#TASK
"""1 = get predictions, 2 = get only features, 3 = train models with new dataset """
TASK = 1

TASK,MINIMUM_SILENCE_DURATION, SIZE_FRAME, SIZE_BETWEEN_FRAMES, NUMBER_OF_ENERGY_POINTS, NUMBER_OF_STABILITY_DISTANCES, PATH_SOUND_FILES, PATH_CSV_FEATURES_FILES, PATH_CSV_RESULTS_FILES, MODEL_NAME = login(TASK, MINIMUM_SILENCE_DURATION, SIZE_FRAME, SIZE_BETWEEN_FRAMES, NUMBER_OF_ENERGY_POINTS, NUMBER_OF_STABILITY_DISTANCES, PATH_SOUND_FILES, PATH_CSV_FEATURES_FILES, PATH_CSV_RESULTS_FILES, MODEL_NAME)

#Get features
if TASK == 1 or TASK ==2:
    number_audios_processed = mainExtractFeatures(PATH_SOUND_FILES, PATH_CSV_FEATURES_FILES, MINIMUM_SILENCE_DURATION, SIZE_FRAME, SIZE_BETWEEN_FRAMES, NUMBER_OF_ENERGY_POINTS, NUMBER_OF_STABILITY_DISTANCES)

    if number_audios_processed ==0:
        print("The folder given in argument does not contain any sound file or all audios have csv files associated")
        sys.exit()

#Get predictions
if TASK ==1:
    number_csv_processed = mainPredict(PATH_CSV_FEATURES_FILES, PATH_CSV_RESULTS_FILES, MODEL_NAME)

    if number_csv_processed ==0:
        print("Nothing was added in the folder csv results")

#Train models with new dataset
if TASK ==3:
    pass

else:
    print("Task number not recognized")

