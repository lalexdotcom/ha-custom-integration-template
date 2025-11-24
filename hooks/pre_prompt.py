import json
import os
import re
import subprocess


def get_repository_url():
    try:
        cwd = os.getcwd()
        os.chdir("..")
        full_url = subprocess.getoutput(["git config --get remote.origin.url"])
        os.chdir(cwd)
        return re.sub(r'(.*)(\.git)$', "\\1", full_url)
    except Exception:
        return False


if __name__ == "__main__":
    github_url = get_repository_url()
    print(github_url)
    if github_url:
        with open("cookiecutter.json", "r+") as file_content:
            data = json.load(file_content)
            data["github_url"] = github_url
            data["code_owner"] = f"@{re.sub(
                r'https://github.com/(.*)/.*', "\\1", github_url)}"
            file_content.seek(0)
            json.dump(data, file_content, indent=4)
            file_content.truncate()
