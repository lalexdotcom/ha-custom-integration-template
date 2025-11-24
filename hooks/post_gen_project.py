import json
from pathlib import Path
import shutil
import os


def move_template():
    working_dir = os.getcwd()
    # folder_entries = os.listdir(os.getcwd())

    # for folder_entry in folder_entries:
    #     shutil.copy(folder_entry, "..")

    for item in os.listdir(working_dir):
        source = os.path.join(working_dir, item)
        target = os.path.join(working_dir, item)
        if os.path.isdir(source):
            shutil.copytree(source, target)
        else:
            os.copy(source, target)
    
    os.rmdir(os.getcwd())


if __name__ == "__main__":
    move_template()
