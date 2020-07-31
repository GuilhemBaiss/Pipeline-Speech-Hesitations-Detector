
from functions.functionsPredict import *
from functions.commonFunctions import *


def mainPredict(path_csv_features_files, path_csv_results, model_name):

    model = load_model(model_name)

    csv_files_list = os.listdir(path_csv_features_files)
    csv_files_processed = 0

    for csv_files in csv_files_list:
        if csv_files[-3:]=="csv":
            csv_files_processed +=1
            if check_if_csv_file_exists(csv_files_list, csv_files):
                path_csv_file = os.path.join(path_csv_features_files, csv_files)
                path_csv_results_file = os.path.join(path_csv_results, csv_files)
                y = get_predictions(model, path_csv_file)
                create_csv(path_csv_file, path_csv_results_file, y)


    #return csv_files_processed
