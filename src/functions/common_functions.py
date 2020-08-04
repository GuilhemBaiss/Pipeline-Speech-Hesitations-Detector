def check_if_csv_file_exists(list_csv, file_name, folder_name):
    """
    Checks if the csv already exists in the csv folder
    params list_csv : list of all the csv files in the csv folder
    params audio_name : audio to check if a csv file already exists
    """
    for csv in list_csv:
        if file_name == csv[:-4] or file_name == csv:
            print("{} already exists in {} folder, do you want to replace it?".format(csv, folder_name))
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