#@Author : Guilhem Baissus
#Algorithm written during an internship at Laboratoire d'ingénierie Cognitive Sémantique (Lincs) located in Montreal, Quebec
#My internship was supervised by Sylvie Ratté
import sys
import os

def login(minimum_silence_duration, size_frame, size_between_frames, number_of_energy_points, number_of_stability_distances, path_to_sound_files, path_to_csv_features_files, path_to_csv_results_file, model_name):

    print("Author : Guilhem Baissus")
    print("Algorithm written during an internship at Laboratoire d'ingénierie Cognitive Sémantique (Lincs) located in Montreal, Quebec. My internship was supervised by Sylvie Ratté")
    print("This algorithm goal is to detect hesitations from sound files using machine learning \n")
    print("[MENU]")
    print("options : \n")
    not_valid_answer1 = True
    while(not_valid_answer1):
        print(" \t [1] : change paths, parameters or model")
        print(" \t [2] : execute without changes")
        print("(1/2) ? ")
        answer1 = input()
        #Change paths, parameters or model
        if "1" in answer1:
            not_valid_answer2 = True
            while(not_valid_answer2):
                print("\n")
                print("options : \n")
                print(" \t [1] : change paths  ")
                print(" \t [2] : change parameters  ")
                print(" \t [3] : change models ")
                print(" \t [4] : execute  ")
                print("(1/2/3/4) ? ")
                answer2 = input()
                #Change paths
                if "1" in answer2:
                    not_valid_answer3 = True
                    while(not_valid_answer3):
                        print("\n")
                        print("the current paths are : \n\t - sound path : {}, \n\t - csv features : {}, \n\t - csv results :  {}".format(path_to_sound_files, path_to_csv_features_files, path_to_csv_results_file))
                        print("options : \n")
                        print(" \t [1] : change sound file path")
                        print(" \t [2] : change csv features path ")
                        print(" \t [3] : change csv results path")
                        print(" \t [4] : done")
                        print("(1/2/3/4) ? ")
                        answer3 = input()

                        if "1" in answer3:
                            print("enter path to sound file : ")
                            path_to_sound_files = input()
                        if "2" in answer3:
                            print("enter path to csv features : ")
                            path_to_csv_features_files = input()
                        if "3" in answer3:
                            print("enter path to csv results : ")
                            path_to_csv_results_file = input()
                        if "4" in answer3:
                            not_valid_answer3 = False
                        else:
                            print("{} is not an option".format(answer3))
                #Change parameters
                if "2" in answer2:
                    not_valid_answer4 = True
                    while(not_valid_answer4):
                        print("\n")
                        print("To understand the parameters, see the documentation")
                        print("the current parameters are : \n\t - minimum silence duration : {}, \n\t - size frame : {}, \n\t - size between frames : {}, \n\t - number energy points : {}, \n\t - number stability distances : {}".format(minimum_silence_duration, size_frame, size_between_frames, number_of_energy_points, number_of_stability_distances))
                        print("options : \n")
                        print(" \t what parameter do you want to modify?")
                        print(" \t [2] : done")
                        print("(name parameter/2) ? ")
                        answer4 = input()

                        if "silence duration" in answer4 or "minimum" in answer4:
                            print("Enter new value for minimum silence duration :")
                            minimum_silence_duration = input()
                        if "size frame" in answer4:
                            print("Enter new value for size frame :")
                            size_frame = input()
                        if "size between frames" in answer4 or "between" in answer4:
                            print("Enter new value for size between frames :")
                            size_between_frames = input()
                        if "number energy points" in answer4 or "energy" in answer4:
                            print("Enter new value for number energy points :")
                            number_of_energy_points = input()
                        if "number stability distances " in answer4 or "stability" in answer4 or "distances" in answer4:
                            print("Enter new value for number stability distances :")
                            number_of_stability_distances = input()
                        if "2" in answer4:
                            not_valid_answer4 = False
                        else:
                            print("{} is not an option".format(answer4))
                #Change models
                if "3" in answer2:
                    not_valid_answer5 = True
                    while(not_valid_answer5):
                        path_to_models = os.path.join(os.getcwd(), "src", "trained_models")
                        trained_models_list = os.listdir(path_to_models)
                        print("\n")
                        print("The following trained models are present :")
                        for models in trained_models_list:
                            if models[-3:] != "txt":
                                print("\t - {}".format(models[:-7]))
                        current_model = model_name
                        print("the current choosen model is {}".format(current_model))
                        print("options : \n")
                        print(" \t What model do you want to choose?")
                        print(" \t [2] : done")
                        print("(name model/2) ? ")
                        answer5 = input()
                        if "2" in answer5:
                            not_valid_answer5 = False
                        else:
                            for models in trained_models_list:
                                if models[-6:] in answer5:
                                    model_name = models[-6:]
                        if current_model == model_name:
                            print("The model was not changed")    
                #Execute
                if "4" in answer2:
                    return minimum_silence_duration, size_frame, size_between_frames, number_of_energy_points, number_of_stability_distances, path_to_sound_files, path_to_csv_features_files, path_to_csv_results_file, model_name
                else : 
                    print("{} is not an option".format(answer2))        
        if "2" in answer1:
            return minimum_silence_duration, size_frame, size_between_frames, number_of_energy_points, number_of_stability_distances, path_to_sound_files, path_to_csv_features_files, path_to_csv_results_file, model_name
        else:
            print("{} is not an option".format(answer1))
    