import os
import shutil

import pandas as pd

def save_to_csv(table_data, output_path):
    """
    Saves table data to a CSV file.

    Args:
        data (list): Table data to save.
        output_csv (str): Path to the output CSV file.
    """
    df = pd.DataFrame(table_data, columns=["Date", "Label", "Value", "Type"])
    df.to_csv(output_path, index=False)
    print(f"Table saved to {output_path}")

def clean_folder(folder_path):
    """
    Remove all files and subdirectories in the given folder.
    If the path is a file, it will be deleted. If the folder does not exist, it will be created.
    """
    if os.path.exists(folder_path):
        if os.path.isfile(folder_path):
            print(f"Deleting file: {folder_path}")
            os.remove(folder_path)  # Remove the file
        else:
            print(f"Cleaning folder: {folder_path}")
            shutil.rmtree(folder_path)  # Remove the folder and its contents

    # Recreate the folder if it was a directory
    if not os.path.isfile(folder_path):
        os.makedirs(folder_path)
        print(f"Folder cleaned and recreated: {folder_path}")
