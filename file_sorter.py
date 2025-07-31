import os
import shutil
from pathlib import Path

PATH_USED = "C:\\Users\\curty\\Documents"


FILETYPES = {"images": ['.jpg', '.jpeg', '.png', '.bmp', '.heic'],
             "documents": ['.pdf', '.docx', '.doc', '.txt', '.ppt', '.pptx'],
             "videos": ['.mp4', '.mkv', '.vi'],
             "audios": ['.mp3', '.wav'],
             "packages": ['.zip']
             }

def create_directory_subfolders(base_path):
    print("Creating subdirectory folders.")
    for file_type in FILETYPES.keys():
        potential_path = os.path.join(base_path, file_type)
        try:
            os.makedirs(potential_path)
        except FileExistsError as e:
            print("This folder already exists: " + str(potential_path))
    
def identify_files(base_path):
    print("\nNow identifying file types.")
    files_sorted = {}
    invalid_types = []
    for file in os.listdir(base_path):
        full_path = os.path.join(base_path, file)
        if os.path.isfile(full_path):
            file_ext = os.path.splitext(file)[1].lower()
            found = False
            for category, file_types in FILETYPES.items():
                if file_ext in file_types:
                    files_sorted[file] = category
                    print(f"Adding '{file}' to '{category}' folder")
                    found = True
                    break
            if not found:
                invalid_types.append(file)
        else:
            print("This is not a file: " + file)
    print(f"Files that are invalid types: {invalid_types}")
    return files_sorted

def move_files(dict_files, source_path):
    print("\nNow moving files into sorted folders.")
    counter = 0
    for file, category in dict_files.items():
        original_path = os.path.join(source_path, file)
        new_dest = os.path.join(source_path, category)
        shutil.move(original_path, new_dest)
        print(f"Moved '{file}' to '{new_dest}")
        counter += 1
    print(f"Moved {counter} files")


if __name__ == "__main__":
    create_directory_subfolders(PATH_USED)
    move_files(identify_files(PATH_USED), PATH_USED)