import shutil
import os


def move_template():
    working_dir = os.listdir(os.getcwd())

    for folder_entry in working_dir:
        shutil.move(folder_entry, "..")

    os.chdir("..")
    os.rmdir(working_dir)


if __name__ == "__main__":
    move_template()
