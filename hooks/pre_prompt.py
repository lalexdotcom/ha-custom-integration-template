import json
import os
import re
import subprocess


def get_repository_url():
    try:
        cwd = os.getcwd()
        os.chdir(os.environ['CUSTOM_INTEGRATION_ROOT'])
        repository_url = re.sub(r'(.*)(\.git)$', "\\1",
                                subprocess.getoutput(["git config --get remote.origin.url"]))
        repository_owner = re.sub(
            r'https://github.com/(.*)/.*', "\\1", repository_url)
        repository_name = re.sub(
            r'https://github.com/.*/(.*)', "\\1", repository_url)
        os.chdir(cwd)

        return {
            "repository_url": repository_url,
            "repository_owner": repository_owner,
            "repository_name": repository_name
        }
    except Exception:
        return False


if __name__ == "__main__":
    repository_infos = get_repository_url()
    if repository_infos:
        with open("cookiecutter.json", "r+") as file_content:
            data = json.load(file_content)
            data["repository_url"] = repository_infos["repository_url"]
            data["repository_owner"] = repository_infos["repository_owner"]
            data["repository_name"] = repository_infos["repository_name"]
            file_content.seek(0)
            json.dump(data, file_content, indent=4)
            file_content.truncate()
