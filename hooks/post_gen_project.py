import shutil
import os


def move_template():
    list_dir = os.listdir(os.getcwd())

    for folder_entry in list_dir:
        shutil.move(folder_entry, "..")


if __name__ == "__main__":
    move_template()
