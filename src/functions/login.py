#@Author : Guilhem Baissus
#Algorithm written during an internship at Laboratoire d'ingénierie Cognitive Sémantique (Lincs) located in Montreal, Quebec
#My internship was supervised by Sylvie Ratté
import sys
import os

def login(task,minimum_silence_duration, size_frame, size_between_frames, number_of_energy_points, number_of_stability_distances, path_to_sound_files, path_to_csv_features_files, path_to_csv_results_file, model_name, path_dataset, path_to_models, path_csv_annotated):

    print("Author : Guilhem Baissus")
    print("Algorithm written during an internship at Laboratoire d'ingénierie Cognitive Sémantique (Lincs) located in Montreal, Quebec. My internship was supervised by Sylvie Ratté")
    print("This algorithm goal is to detect hesitations from sound files using machine learning \n")
    print("[MENU]")
    not_valid_answer1 = True
    while(not_valid_answer1):
        print("options : \n")
        print(" \t [1] : change paths, parameters or model")
        print(" \t [2] : stay with the default configurations")
        print("(1/2) ? ")
        answer1 = input()
        #Change paths, parameters or model
        if "1" in answer1 and len(answer1) < 2:
            not_valid_answer2 = True
            while(not_valid_answer2):
                print("options : \n")
                print(" \t [1] : change paths  ")
                print(" \t [2] : change parameters  ")
                print(" \t [3] : change models ")
                print(" \t [4] : go back to options  ")
                print("(1/2/3/4) ? ")
                answer2 = input()
                #Change paths
                if "1" in answer2 and len(answer2)<2:
                    not_valid_answer3 = True
                    while(not_valid_answer3):
                        print("the current paths are : \n\t - sound path : {}, \n\t - csv features : {}, \n\t - csv results :  {},  \n\t - path to dataset :  {},  \n\t - path to trained models:  {}, \n\t - path to annotated csv:  {}".format(path_to_sound_files, path_to_csv_features_files, path_to_csv_results_file, path_dataset, path_to_models, path_csv_annotated))
                        print("options : \n")
                        print(" \t [1] : change sound file folder path")
                        print(" \t [2] : change csv features folder path ")
                        print(" \t [3] : change csv results folder path")
                        print(" \t [4] : change dataset folder path")
                        print(" \t [5] : change trained models folder path")
                        print(" \t [6] : change annotated csv folder path")
                        print(" \t [7] : done")
                        print("(1/2/3/4/5/6/7) ? ")
                        answer3 = input()
                        if "1" in answer3 and len(answer3) < 2:
                            print("enter path to sound file : ")
                            path_to_sound_files = input()
                        elif "2" in answer3 and len(answer3) < 2:
                            print("enter path to csv features : ")
                            path_to_csv_features_files = input()
                        elif "3" in answer3 and len(answer3) < 2:
                            print("enter path to csv results : ")
                            path_to_csv_results_file = input()
                        elif "4" in answer3 and len(answer3) <2:
                            print("enter path to the dataset file : ")
                            path_dataset = input()
                        elif "5" in answer3 and len(answer3) <2:
                            print("enter path to the trained models folder : ")
                            path_to_models = input()
                        elif "6" in answer3 and len(answer3) <2:
                            print("enter path to the annotated csv folder : ")
                            path_to_models = input()
                        elif "7" in answer3 and len(answer3) < 2:
                            not_valid_answer3 = False
                        else:
                            print("{} is not an option".format(answer3))
                #Change parameters
                elif "2" in answer2 and len(answer2) < 2 :
                    not_valid_answer4 = True
                    while(not_valid_answer4):
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
                        elif "size frame" in answer4:
                            print("Enter new value for size frame :")
                            size_frame = input()
                        elif "size between frames" in answer4 or "between" in answer4:
                            print("Enter new value for size between frames :")
                            size_between_frames = input()
                        elif "number energy points" in answer4 or "energy" in answer4:
                            print("Enter new value for number energy points :")
                            number_of_energy_points = input()
                        elif "number stability distances " in answer4 or "stability" in answer4 or "distances" in answer4:
                            print("Enter new value for number stability distances :")
                            number_of_stability_distances = input()
                        elif "2" in answer4:
                            not_valid_answer4 = False
                        else:
                            print("{} is not an option".format(answer4))
                #Change models
                elif "3" in answer2 and len(answer2) < 2:
                    not_valid_answer5 = True
                    while(not_valid_answer5):
                        trained_models_list = os.listdir(path_to_models)
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
                        if "2" in answer5 and len(answer5) < 2:
                            not_valid_answer5 = False
                        else:
                            for models in trained_models_list:
                                if models[:-7] in answer5:
                                    model_name = models[:7]
                        if current_model == model_name:
                            print("The model was not changed")    
                #go back to options
                elif "4" in answer2 and len(answer2) < 2:
                    not_valid_answer2 =  False
                else:
                    print("{} is not an option".format(answer2))       
        #Choose task 
        elif "2" in answer1 and len(answer1) <2:
            not_valid_answer6 = True
            while(not_valid_answer6):
                print("options : \n")
                print(" \t [1] : get filled pauses from the sound files in a csv")
                print(" \t [2] : get features from the sound files")
                print(" \t [3] : create new dataset and train models")
                print("(1/2/3) ? ")
                answer6 = input()
                #get filled pauses
                if "1" in answer6 and len(answer6) <2:
                    task =1
                    return task, minimum_silence_duration, size_frame, size_between_frames, number_of_energy_points, number_of_stability_distances, path_to_sound_files, path_to_csv_features_files, path_to_csv_results_file, model_name, path_dataset, path_to_models, path_csv_annotated
                #get only features
                elif "2" in answer6 and len(answer6) <2:
                    task =2
                    return task, minimum_silence_duration, size_frame, size_between_frames, number_of_energy_points, number_of_stability_distances, path_to_sound_files, path_to_csv_features_files, path_to_csv_results_file, model_name, path_dataset, path_to_models, path_csv_annotated
                #create new dataset and train models
                elif "3" in answer6 and len(answer6) <2:
                    task =3
                    return task, minimum_silence_duration, size_frame, size_between_frames, number_of_energy_points, number_of_stability_distances, path_to_sound_files, path_to_csv_features_files, path_to_csv_results_file, model_name, path_dataset, path_to_models, path_csv_annotated
                else:
                    print("{} is not an option".format(answer6))

        else:
            print("{} is not an option".format(answer1))
    