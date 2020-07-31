#@Author : Guilhem Baissus
#Algorithm written during an internship at Laboratoire d'ingénierie Cognitive Sémantique (Lincs) located in Montreal, Quebec
#My internship was supervised by Sylvie Ratté
import sys

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

                if "1" in answer2:
                    not_valid_answer3 = True
                    while(not_valid_answer3):
                        print("\n")
                        print("the current paths are : \n\t - sound path : {}, \n\t - csv features : {}, \n\t - csv results :  {}".format(path_to_sound_files, path_to_csv_features_files, path_to_csv_results_file))
                        print("options : \n")
                        print(" \t [1] : change sound file path")
                        print(" \t [2] : change csv features path ")
                        print(" \t [3] : change csv results path")
                        print(" \t [4] : execute")
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

                if "2" in answer2:
                    not_valid_answer4 = True
                    while(not_valid_answer4):
                        print("\n")
                        print("options : \n")
                        print(" \t [1] : change paths")
                        print(" \t [2] : change parameters")
                        print(" \t [3] : change models")
                        print(" \t [4] : execute without changes")
                        print("(1/2/3/4) ? ")
                        answer4 = input()
                if "3" in answer2:
                    pass
                else : 
                    print("{} is not an option".format(answer2))
            
        if "2" in answer1:
            return minimum_silence_duration, size_frame, size_between_frames, number_of_energy_points, number_of_stability_distances, path_to_sound_files, path_to_csv_features_files, path_to_csv_results_file, model_name
        else:
            print("{} is not an option".format(answer1))
    




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