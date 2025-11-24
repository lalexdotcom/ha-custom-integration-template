import json
import os
import re
import subprocess


def get_repository_url():
    try:
        cwd = os.getcwd()
        print("cwd is %s", cwd)
        os.chdir("..")
        print("Get repository URL from %s", os.getcwd())
        full_url = re.sub(r'(.*)(\.git)$', "\\1",
                          subprocess.getoutput(["git config --get remote.origin.url"]))
        os.chdir(cwd)
        return {
            "repository_url": full_url,
            "github_code_owner": f"@{re.sub(
                r'https://github.com/(.*)/.*', "\\1", full_url)}"
        }
    except Exception:
        return False


if __name__ == "__main__":
    print(os.environ['CUSTOM_INTEGRATION_ROOT'])
    repository_infos = get_repository_url()
    print(repository_infos)
    if repository_infos:
        with open("cookiecutter.json", "r+") as file_content:
            data = json.load(file_content)
            data["github_url"] = repository_infos["repository_url"]
            data["code_owner"] = repository_infos["github_code_owner"]
            file_content.seek(0)
            json.dump(data, file_content, indent=4)
            file_content.truncate()
