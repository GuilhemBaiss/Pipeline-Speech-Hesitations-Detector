#@Author : Guilhem Baissus
#Algorithm written during an internship at Laboratoire d'ingénierie Cognitive Sémantique (Lincs) located in Montreal, Quebec
#My internship was supervised by Sylvie Ratté

import os
import pandas as pd
from functions.functionsFeatures import *

def check_os(path, audios_names):
    """
    Method that returns the path to a precise audio file depending of the user's operating system
    params path : path to the folder containing the sound files
    params audios_name : name of the sound file that the algorithm is going to analyse
    returns : path to the specific audio file. 
    """
    if "/" in path and "\\" is not True:
        path_sound_file = path + "/" + audios_names
    else:
        path_sound_file = path + "\\" + audios_names
    return path_sound_file

def check_if_csv_file(list_csv, audio_name):
    """
    Checks if the csv already exists in the csv folder
    params list_csv : list of all the csv files in the csv folder
    params audio_name : audio to check if a csv file already exists
    """
    for csv in list_csv:
        if audio_name == csv[:-4]:
            print("{} already exists".format(csv))
            return False
    return True
#-----------------------------------------------------------------------------------------------------------

def mainExtractFeatures(path_sound_files, path_csv_files, minimum_silence_duration = 0.1, size_frame = 0.5, size_between_frames = 0.1, number_of_energy_points = 100, number_of_stability_distances = 10):
    data = {}
    df = pd.DataFrame()

    audio_files_list = os.listdir(path_sound_files)
    csv_files_list = os.listdir(path_csv_files)

    number_audios_processed = 0 
    size_audios_folder = len(audio_files_list)

    for audios_names in audio_files_list:
        if audios_names[-3:] == "mp3" or audios_names[-3:] == "wav" or audios_names[-3:] == "MP3" or audios_names[-3:] == "WAV" :
            number_audios_processed +=1
            if check_if_csv_file(csv_files_list, audios_names):
                path_sound_file = check_os(path_sound_files, audios_names)
                print("Processing file : {} - {}/{}".format(audios_names, number_audios_processed, size_audios_folder))
                data = ExtractFeatures.extract_features(path_sound_file, minimum_silence_duration=minimum_silence_duration, size_frame=size_frame, size_between_frames=size_between_frames, number_of_energy_points=number_of_energy_points, number_of_distances=number_of_stability_distances)
                df = pd.DataFrame(data,columns=list(data.keys()))
                df.to_csv(path_csv_files + "\{}.csv".format(audios_names), index = False)

    return number_audios_processed
    






