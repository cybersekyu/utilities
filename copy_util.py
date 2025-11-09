import shutil
import os
import time

# Define the source directory where the files are located
source_directory = "/file/path"
# Define the destination directory where you want to copy the files
destination_directory = "/file/path"

# Create a list of filenames you want to copy
# This could be generated dynamically using os.listdir() or os.walk()
# or hardcoded as a list.
filenames_to_copy = open("text file", 'r')

# Ensure the destination directory exists; create it if it doesn't
#os.makedirs(destination_directory, exist_ok=True)

# Loop through each filename in the list
for filename in filenames_to_copy:
    fpath = filename.strip()
    source_path = os.path.join(source_directory, fpath)
    destination_path = os.path.join(destination_directory, fpath)

    # Check if the source file exists before attempting to copy
    if os.path.isdir(source_path):
        shutil.copytree(source_path, destination_path)
        print(f"Copied Directory '{fpath}' to '{destination_path}'")
    elif os.path.exists(source_path):
        shutil.copy(source_path, destination_directory)
        print(f"Copied '{fpath}' to '{destination_directory}'")
    else:
        print(f"Warning: Source file '{fpath}' not found in '{source_directory}'")
    # adding a delay to not overwhelm server
    print("Waiting for 30 minutes")
    time.sleep(1800)