import json
import subprocess


def get_repository_url():
    try:
        return subprocess.getoutput(["git config --get remote.origin.url"])
    except Exception:
        return False


if __name__ == "__main__":
    github_url = get_repository_url()
    print(github_url)
    if github_url:
        with open('cookiecutter.json', 'r+') as file_content:
            data = json.load(file_content)
            data['github_url'] = github_url # <--- add `id` value.
            file_content.seek(0)        # <--- should reset file position to the beginning.
            json.dump(data, file_content, indent=4)
            file_content.truncate()     # remove remaining part
