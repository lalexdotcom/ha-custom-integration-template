import shutil
import os


def move_template():
    cur_dir = os.getcwd()  # current dir path
    tmp_dir = os.path.join(cur_dir, "{{cookiecutter.project_name}}")
    list_dir = os.listdir(tmp_dir)
    dest = cur_dir

    for folder_entry in list_dir:
        shutil.move(tmp_dir, dest)


if __name__ == "__main__":
    move_template()
