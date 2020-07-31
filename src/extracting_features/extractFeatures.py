#@Author : Guilhem Baissus
#Algorithm written during an internship at Laboratoire d'ingénierie Cognitive Sémantique (Lincs) located in Montreal, Quebec
#My internship was supervised by Sylvie Ratté

import os
import pandas as pd
from extracting_features.functionsFeatures import *
from functions.commonFunctions import *


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
            if check_if_csv_file_exists(csv_files_list, audios_names):
                path_sound_file = os.path.join(path_sound_files, audios_names)
                print("Processing file : {} - {}/{}".format(audios_names, number_audios_processed, size_audios_folder))
                data = ExtractFeatures.extract_features(path_sound_file, minimum_silence_duration=minimum_silence_duration, size_frame=size_frame, size_between_frames=size_between_frames, number_of_energy_points=number_of_energy_points, number_of_distances=number_of_stability_distances)
                df = pd.DataFrame(data,columns=list(data.keys()))
                df.to_csv(path_csv_files + "\{}.csv".format(audios_names), index = False)

    return number_audios_processed
    






