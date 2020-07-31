
import sys
import os
from extractFeatures import *
from predict import *

#-----------------------------------------------------------------------------------------------------------
#HYPERPARAMETERS 
MINIMUM_SILENCE_DURATION = 0.1
SIZE_FRAME = 0.5
SIZE_BETWEEN_FRAMES = 0.1
NUMBER_OF_ENERGY_POINTS = 100
NUMBER_OF_STABILITY_DISTANCES = 10

PATH_SOUND_FILES = os.path.join(os.getcwd(), "audios")
PATH_CSV_FEATURES_FILES = os.path.join(os.getcwd(), "csv-features")
PATH_CSV_RESULTS_FILES = os.path.join(os.getcwd(), "csv-results")
MODEL_NAME = "decision_tree_model"

print("python pythonFile.py [path_to_sound_files]")
#Look if the path is given by argument
if len(sys.argv) ==2:
    PATH_SOUND_FILES = sys.argv[1]

# if len(sys.argv) == 3:
#     PATH_SOUND_FILES =sys.argv[1]
#     PATH_CSV_FILES = sys.argv[2]

elif len(sys.argv) > 2:
    print("Error too many arguments given")
    sys.exit()

number_audios_processed = mainExtractFeatures(PATH_SOUND_FILES, PATH_CSV_FEATURES_FILES, MINIMUM_SILENCE_DURATION, SIZE_FRAME, SIZE_BETWEEN_FRAMES, NUMBER_OF_ENERGY_POINTS, NUMBER_OF_STABILITY_DISTANCES)

if number_audios_processed ==0:
        print("The folder given in argument does not contain any sound file or all audios have csv files associated")
        sys.exit()

mainPredict(PATH_CSV_FEATURES_FILES, PATH_CSV_RESULTS_FILES, MODEL_NAME)

