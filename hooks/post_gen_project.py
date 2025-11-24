import shutil
import os


def move_template():
    folder_entries = os.listdir(os.getcwd())

    for folder_entry in folder_entries:
        shutil.move(folder_entry, "..")

    os.rmdir(os.getcwd())


if __name__ == "__main__":
    move_template()
