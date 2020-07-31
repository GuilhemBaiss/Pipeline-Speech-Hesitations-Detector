#@Author : Guilhem Baissus
#Algorithm written during an internship at Laboratoire d'ingénierie Cognitive Sémantique (Lincs) located in Montreal, Quebec
#My internship was supervised by Sylvie Ratté

import sys
import os
from extracting_features.extractFeatures import *
from returning_predictions.predict import *
from functions.login import *

#-----------------------------------------------------------------------------------------------------------
#HYPERPARAMETERS 
MINIMUM_SILENCE_DURATION = 0.1
SIZE_FRAME = 0.5
SIZE_BETWEEN_FRAMES = 0.1
NUMBER_OF_ENERGY_POINTS = 100
NUMBER_OF_STABILITY_DISTANCES = 10

#PATHS BY DEFAULT
PATH_SOUND_FILES = os.path.join(os.getcwd(), "audios")
PATH_CSV_FEATURES_FILES = os.path.join(os.getcwd(), "csv-features")
PATH_CSV_RESULTS_FILES = os.path.join(os.getcwd(), "csv-results")
MODEL_NAME = "decision_tree_model"

MINIMUM_SILENCE_DURATION, SIZE_FRAME, SIZE_BETWEEN_FRAMES, NUMBER_OF_ENERGY_POINTS, NUMBER_OF_STABILITY_DISTANCES, MODEL_NAME = login(MINIMUM_SILENCE_DURATION, SIZE_FRAME, SIZE_BETWEEN_FRAMES, NUMBER_OF_ENERGY_POINTS, NUMBER_OF_STABILITY_DISTANCES, PATH_SOUND_FILES, PATH_CSV_FEATURES_FILES, PATH_CSV_RESULTS_FILES, MODEL_NAME)

# number_audios_processed = mainExtractFeatures(PATH_SOUND_FILES, PATH_CSV_FEATURES_FILES, MINIMUM_SILENCE_DURATION, SIZE_FRAME, SIZE_BETWEEN_FRAMES, NUMBER_OF_ENERGY_POINTS, NUMBER_OF_STABILITY_DISTANCES)

# if number_audios_processed ==0:
#         print("The folder given in argument does not contain any sound file or all audios have csv files associated")
#         sys.exit()

# number_csv_processed = mainPredict(PATH_CSV_FEATURES_FILES, PATH_CSV_RESULTS_FILES, MODEL_NAME)

# if number_csv_processed ==0:
#     print("Nothing was added in the folder csv results")

