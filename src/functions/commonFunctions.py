def check_if_csv_file_exists(list_csv, file_name):
    """
    Checks if the csv already exists in the csv folder
    params list_csv : list of all the csv files in the csv folder
    params audio_name : audio to check if a csv file already exists
    """
    for csv in list_csv:
        if file_name == csv[:-4]:
            print("{} already exists".format(csv))
            return False
    return True