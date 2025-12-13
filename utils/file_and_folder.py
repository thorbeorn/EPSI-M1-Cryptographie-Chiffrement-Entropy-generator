import os

def init_File_And_Folder(TEMP_OUTPUT, OUTPUT) :
    try:
        os.makedirs(TEMP_OUTPUT["temp_folder"], exist_ok=True)
        os.makedirs(OUTPUT["folder"], exist_ok=True)
    except Exception as e :
        raise(e)

def remove_Temp_File(TEMP_OUTPUT) :
    try:
        for filename in os.listdir(TEMP_OUTPUT["temp_folder"]):
            file_path = os.path.join(TEMP_OUTPUT["temp_folder"], filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
    except Exception as e :
        raise(e)