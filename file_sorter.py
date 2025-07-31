import os
import shutil
from pathlib import Path

PATH_USED = ""


FILETYPES = {"images": ['.jpg', '.jpeg', '.png', '.bmp', '.heic'],
             "documents": ['.pdf', '.docx', '.doc', '.txt', '.ppt', '.pptx'],
             "videos": ['.mp4', '.mkv', '.vi'],
             "audios": ['.mp3', '.wav'],
             "packages": ['.zip']
             }

def create_directory_subfolders(base_path):
    for file_type in FILETYPES.keys():
        potential_path = Path(base_path + "\\" + file_type)
        try:
            os.makedirs(potential_path)
        except FileExistsError as e:
            print("This folder already exists: " + str(potential_path))
    
def identify_files(base_path):
    files_sorted = {}
    for file in os.listdir(base_path):
        full_path = os.path.join(base_path, file)
        if os.path.isfile(full_path):
            for category, file_types in FILETYPES.items():
                for specific_type in file_types:
                    if os.path.splitext(file)[1] in specific_type:
                        files_sorted[file] = category
                        print(f"Adding '{file}' to '{category}' folder")
                    else:
                        print(f"'{file}' is not within the '{category}' folder")
                        break
        else:
            print("This is not a file: " + file)
    return files_sorted

def move_files(dict_files, source_path):
    for file, category in dict_files.items():
        original_path = Path(source_path + "\\" + file)
        new_dest = Path(source_path + "\\" + category)
        shutil.move(original_path, new_dest)
        print(f"Moved '{file}' to '{new_dest}")


if __name__ == "__main__":
    create_directory_subfolders(PATH_USED)
    move_files(identify_files(PATH_USED), PATH_USED)