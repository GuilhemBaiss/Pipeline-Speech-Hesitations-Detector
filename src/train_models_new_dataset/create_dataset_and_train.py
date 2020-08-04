#@Author : Guilhem Baissus
#Algorithm written during an internship at Laboratoire d'ingénierie Cognitive Sémantique (Lincs) located in Montreal, Quebec
#My internship was supervised by Sylvie Ratté

from train_models_new_dataset.functions_dataset_models import *
from train_models_new_dataset.random_forest_model import *
from train_models_new_dataset.svm_model import *
from train_models_new_dataset.decision_tree_model import *

def if_in_folder(name_file, files_list, file_name):
    for files in files_list:
        if name_file in files:
            print("{} already exists in {} folder, do you want to replace it?".format(name_file, file_name))
            not_valid_answer = True
            while(not_valid_answer):
                print("(y/n ?)")
                answer = input()
                if "y" in answer and len(answer)<2:
                    return False
                elif "n" in answer and len(answer)<2:
                    return True
                else:
                    print("{} is not an option".format(answer))
    return False

def mainCreateDataset(path_csv_files, path_dataset, dataset_name):
    """
    Creates new dataset
    params path_csv_files : path to the csv files used to create the new dataset
    params path_dataset : path to the new dataset
    params dataset_name : name of the new dataset
    """

    Dataset.create_dataset(path_csv_files, path_dataset, dataset_name)

def mainTrainModels(path_to_dataset, path_to_models, model_name, criterion = "entropy", number_of_trees = 100, max_features = 'sqrt', kernel = "linear"):
    """
    Trains a model 
    params path_models_files : where to save the new models
    params path_dataset : where to get the dataset used to train the models
    params dataset_name : the name of the dataset used to train the models
    params model_name : the model that we want to train
    """
    models_files_list = os.listdir(path_to_models)
    if not if_in_folder(model_name + ".pickle", models_files_list, "models"):
        if model_name == "decision_tree_model":
            mainDecisionTree(path_to_dataset, path_to_models, criterion)

        elif model_name == "random_forest_model":
            mainRandomForestClassifier(path_to_dataset, path_to_models, number_of_trees, max_features)

        elif model_name == "svm_model":
            mainSVMModel(path_to_dataset, path_to_models, kernel)

        print("the model {} was trained with success".format(model_name))
        print("you can found the accuracy in the accuracy_score.txt file \n")

