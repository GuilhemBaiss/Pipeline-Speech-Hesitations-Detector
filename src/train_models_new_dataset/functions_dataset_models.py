#@Author : Guilhem Baissus
#Algorithm written during an internship at Laboratoire d'ingénierie Cognitive Sémantique (Lincs) located in Montreal, Quebec
#My internship was supervised by Sylvie Ratté

import pandas as pd
import os
import random
import numpy as np
import sklearn
import matplotlib.pyplot as plt 
import itertools
from sklearn.metrics import plot_confusion_matrix

# def get_confusion_matrix(path_dataset, model, xtest, ytest, normalize=False, title='Confusion matrix'):
#     # Plot non-normalized confusion matrix
#     plt.figure()
#     data = pd.read_csv(path_dataset, sep=",")
#     data = data.drop("classification", axis = 1)
#     classes = ["NFP", "FP"]
#     titles_options = [("Confusion matrix, without normalization", None),
#                     ("Normalized confusion matrix", 'true')]
#     for title, normalize in titles_options:
#         disp = plot_confusion_matrix(model, xtest, ytest,
#                                     display_labels=classes,
#                                     cmap=plt.cm.get_cmap("Blues"),
#                                     normalize=normalize)
#         disp.ax_.set_title(title)

#         print(title)
#         print(disp.confusion_matrix)

#     plt.show()
    

class Dataset:

    @staticmethod
    def get_data(path_dataset, test_size = 0.1):
        """
        returns xtrain, xtest, xvalidation, ytrain, ytest, yvalidation from dataset
        """
        data = pd.read_csv(path_dataset, sep=",")
        predict = "classification"
        X = np.array(data.drop(predict, axis=1))
        y = np.array(data[predict])

        xtrain, xtest, ytrain, ytest = sklearn.model_selection.train_test_split(X, y, test_size=test_size)

        return xtrain, xtest, ytrain, ytest


    @staticmethod
    def create_dataset(path_csv_files, path_dataset, name_dataset):
        """
        creates a csv file containing 50% of filled pauses and 50% of non filled pauses
        params path_csv_files : path to the csv files folder
        params path_dataset : path to where to find the created dataset file
        params name_dataset : name of the created dataset
        """
        dataset_files_list = os.listdir(path_dataset)
        if name_dataset + ".csv" in dataset_files_list:
            print("{} already exists in the dataset folder , do you want to replace it?".format(name_dataset + ".csv"))
            not_valid_answer = True
            while(not_valid_answer):
                print("(y/n ?)")
                answer = input()
                if "y" in answer and len(answer)<2:
                    dataset = pd.DataFrame(columns=Functions.get_columns(path_csv_files))
                    dataset = Dataset.adding_NFP_to_dataset(path_csv_files, dataset)
                    dataset = Dataset.adding_FP_to_dataset(path_csv_files, dataset)
                    dataset = dataset.drop(["start_time","end_time"], axis = 1)
                    dataset.to_csv(os.path.join(path_dataset, "{}.csv".format(name_dataset)), index = False)
                    Dataset.create_file_statistics(path_csv_files, path_dataset, name_dataset)    
                elif "n" in answer and len(answer)<2:
                    print("{} already exists and will not be replaced".format(name_dataset + ".csv"))
                    not_valid_answer = False
                else:
                    print("{} is not an option".format(answer))


    @staticmethod
    def create_file_statistics(path_csv_files, path_dataset, name_dataset):
        """
        Creates a text file in the dataset folder and writes some statistics about the created dataset and the csv files used
        params path_csv_files : path to the csv files folder
        params path_dataset : path to where to find the created dataset file
        params name_dataset : name of the created dataset
        """
        f= open(os.path.join(path_dataset, "{}_statistics.txt".format(name_dataset)),"w+")
        f.write("Statistics of '{}': \n ".format(name_dataset))
        f.write("\n ")
        size = Data_statistics.total_number_FP_in_csv_files(path_csv_files) * 2
        f.write("dataset size : {} \n".format(size))
        f.write("number of FP in dataset : {} \n".format(size/2))
        f.write("number of NFP in dataset : {} \n".format(size/2))
        f.write("\n ")
        f.write("Statistics from all the csv files used to create '{}' \n".format(name_dataset))
        f.write("\n ")
        f.write("number of csv files in the folder : {} \n".format(Data_statistics.total_csv_files(path_csv_files)))
        f.write("total number of FP : {} \n".format(size/2))
        f.write("total number of NFP : {} \n".format(Data_statistics.total_number_NFP_in_csv_files(path_csv_files)))
        f.write("average number of FP per csv file : {} \n".format(Data_statistics.average_number_FP_csv(path_csv_files)))
        f.write("average number of NFP per csv file : {} \n".format(Data_statistics.average_number_NFP_csv(path_csv_files)))
        f.close()

    @staticmethod
    def adding_NFP_to_dataset(path_csv_files, dataset):
        """
        Adds the amount of FP of NFP in the dataset.
        """
        number_FP = Data_statistics.total_number_FP_in_csv_files(path_csv_files)
        number_csv_files = Data_statistics.total_csv_files(path_csv_files)

        number_NFP_per_csv = int(number_FP / number_csv_files)
        rest_NFP = number_FP - number_NFP_per_csv * number_csv_files

        csv_files_list = os.listdir(path_csv_files)

        #To prevent the same NFP used twice, it will contain list of indexes for every csv file
        all_csv_indexes_used = []

        #Adding number_NFP_per_csv in the dataset 
        for csv in csv_files_list:
            if csv[-3:] == "csv":
                csv_indexes_used = []

                path_csv_file = os.path.join(path_csv_files, "{}".format(csv))
                data = pd.read_csv(path_csv_file,sep = ",")
                size_csv_file = len(data["classification"])

                #Check if the number of NFP in the file is higher than the number required per csv
                number_lines_extracted = number_NFP_per_csv
                total_NFP_in_file = Data_statistics.total_number_NFP_in_csv_file(path_csv_file)
                if number_NFP_per_csv > total_NFP_in_file:
                    number_lines_extracted = total_NFP_in_file
                    rest_NFP += number_csv_files - total_NFP_in_file

                for rows in range(0, number_lines_extracted):
                    row_index = random.randrange(0, size_csv_file, 1)
                    while(data["classification"][row_index] =="FP" or row_index in csv_indexes_used):
                        row_index = random.randrange(0, size_csv_file, 1)
                    csv_indexes_used.append(row_index)
                    row = data.loc[ row_index ,:]
                    dataset.loc[len(dataset)] = row
            all_csv_indexes_used.append(csv_indexes_used)

        #Adding rest_NFP
        if rest_NFP!=0 :
            for i in range(0,rest_NFP):
                csv_file_position = random.randrange(0, number_csv_files, 1)
                path_to_csv_file = os.path.join(path_csv_files, "{}".format(csv_files_list[csv_file_position]))

                #check if csv file and if NFP extracted not equal to the number of indexes already extracted
                while(csv_files_list[csv_file_position][-3:] != "csv" or Data_statistics.total_number_NFP_in_csv_file(path_to_csv_file) == len(all_csv_indexes_used[csv_file_position])):
                    csv_file_position = random.randrange(0, number_csv_files, 1)
                    path_to_csv_file = path_csv_files + "\{}".format(csv_files_list[csv_file_position])

                data = pd.read_csv(path_to_csv_file,sep = ",")
                size_csv_file = len(data["classification"])
                row_index = random.randrange(0, size_csv_file, 1)
                while(data["classification"][row_index] =="FP" or row_index in all_csv_indexes_used[csv_file_position]):
                    row_index = random.randrange(0, size_csv_file, 1)
                row = data.loc[ row_index ,:]
                dataset.loc[len(dataset)] = row
                all_csv_indexes_used[csv_file_position].append(row_index)

        return dataset

    @staticmethod
    def adding_FP_to_dataset(path_csv_files, dataset):
        """
        """
        csv_files_list = os.listdir(path_csv_files)

        for csv in csv_files_list:
            if csv[-3:] == "csv":
                data = pd.read_csv(os.path.join(path_csv_files, "{}".format(csv)),sep = ",")
                for row_index in range(0, len(data["classification"])):
                    if data["classification"][row_index]=="FP":
                        row = data.loc[ row_index ,:]
                        dataset.loc[len(dataset)] = row
        return dataset

class Data_statistics:
    
    @staticmethod
    def total_number_FP_in_csv_files(path_csv_files):
        """
        returns the total number of filled pauses contained in all the csv files. It will represent 50% of our dataset 
        """
        csv_files_list = os.listdir(path_csv_files)
        number_FP = 0

        for csv in csv_files_list:
            if csv[-3:] == "csv":
                data = pd.read_csv(os.path.join(path_csv_files, "{}".format(csv)),sep = ",")
                data = data["classification"]
                for values in data:
                    if values == "FP":
                        number_FP += 1

        return number_FP
    
    @staticmethod
    def total_csv_files(path_csv_files):
        csv_files_list = os.listdir(path_csv_files)
        number = 0

        for csv in csv_files_list:
            if csv[-3:] == "csv":
                number +=1
        
        return number

    @staticmethod
    def total_number_NFP_in_csv_files(path_csv_files):
        """
        returns the total number of filled pauses contained in all the csv files. It will represent 50% of our dataset 
        """
        csv_files_list = os.listdir(path_csv_files)
        number_NFP = 0

        for csv in csv_files_list:
            if csv[-3:] == "csv":
                data = pd.read_csv(os.path.join(path_csv_files, "{}".format(csv)),sep = ",")
                data = data["classification"]
                for values in data:
                    if values == "NFP":
                        number_NFP += 1
        return number_NFP

    @staticmethod
    def total_number_NFP_in_csv_file(path_csv_file):
        """
        returns the total number of filled pauses contained in all the csv files. It will represent 50% of our dataset 
        """
        number_NFP = 0

        data = pd.read_csv(path_csv_file,sep = ",")
        data = data["classification"]
        for values in data:
            if values == "NFP":
                number_NFP += 1

        return number_NFP

    @staticmethod
    def average_number_FP_csv(path_csv_files):
        """
        """
        csv_files_list = os.listdir(path_csv_files)
        average_FP = 0
        size = 0

        for csv in csv_files_list:
            if csv[-3:] == "csv":
                size += 1
                data = pd.read_csv(os.path.join(path_csv_files, "{}".format(csv)),sep = ",")
                data = data["classification"]
                number_FP_csv = 0
                for values in data:
                    if values == "FP":
                        number_FP_csv += 1
                average_FP += number_FP_csv

        return average_FP /size

    @staticmethod
    def average_number_NFP_csv(path_csv_files):
        """
        """
        csv_files_list = os.listdir(path_csv_files)
        average_NFP = 0
        size = 0

        for csv in csv_files_list:
            if csv[-3:] == "csv":
                size += 1
                data = pd.read_csv(os.path.join(path_csv_files, "{}".format(csv)),sep = ",")
                data = data["classification"]
                number_FP_csv = 0
                for values in data:
                    if values == "NFP":
                        average_NFP += 1
                average_NFP += number_FP_csv

        return average_NFP /size

class Functions:

        @staticmethod
        def get_columns(path_csv_files):
            csv_files_list = os.listdir(path_csv_files)
            index = 0
            while(csv_files_list[index][-3:] != "csv"):
                index +=1
            data = pd.read_csv(os.path.join(path_csv_files, "{}".format(csv_files_list[index])),sep = ",")
            return data.columns
        
        @staticmethod
        def write_accuracy_score_text_file(path_to_models, model_name, accuracy_score):
            """
            Writes accuracy in accuracy.score.txt 
            params path_to_models : path to the trained models files
            params model_name : name of the model newly trained
            params accuracy_score : accuracy score the new trained model
            """
            files = os.listdir(path_to_models)
            if "accuracy_scores.txt" in files:
                f = open(os.path.join(path_to_models,"accuracy_scores.txt"))
                text_in_file = f.readlines()
                f.close()
                present_in_file = False
                for index,line in enumerate(text_in_file):
                    if model_name in line:
                        present_in_file = True
                        text_in_file[index] = model_name + " : {} \n".format(accuracy_score)
                #Should never happen
                if present_in_file == False:
                    print("Did not find model in accuracy_scores.txt")
                    text_in_file.append(model_name + " : {}\n".format(accuracy_score))

                f = open(os.path.join(path_to_models,"accuracy_scores.txt"), "w")
                new_file_contents = "".join(text_in_file)
                f.write(new_file_contents)
                f.close()
            else:
                f= open(os.path.join(path_to_models, "accuracy_scores.txt"),"w+")
                f.write (model_name + " : {} \n".format(accuracy_score))
                f.close

        # @staticmethod
        # def show_duplicates(dataset):
        #     duplicateDFRow = dataset[dataset.duplicated(keep='last')]
        #     print(duplicateDFRow)
        #     duplicateDF = dataset[dataset.duplicated()]
        #     print(duplicateDF)








