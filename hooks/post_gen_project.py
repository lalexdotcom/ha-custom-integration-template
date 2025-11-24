import shutil
import os


def move_template():
    MOVE_PATHS = [
        "custom_components",
        "scripts",
        
    ]

    for path in MOVE_PATHS:
        path = path.strip()
        if path and os.path.exists(path):
            os.unlink(path) if os.path.isfile(path) else os.rmdir(path)

    list_dir = os.listdir(os.getcwd())

    shutil.move("custom_components", "..")
    shutil.move(".github", "..")


if __name__ == "__main__":
    move_template()
