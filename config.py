import json
import shutil


CONFIG_FILE = "groups.json"
BACKUP_FILE = "groups.backup.json"


def load_groups():

    with open(CONFIG_FILE, "r", encoding="utf-8") as file:

        data = json.load(file)

    return data.get("groups", [])


def save_groups(groups):

    try:

        shutil.copyfile(
            CONFIG_FILE,
            BACKUP_FILE
        )

    except FileNotFoundError:

        pass

    with open(CONFIG_FILE, "w", encoding="utf-8") as file:

        json.dump(
            {"groups": groups},
            file,
            ensure_ascii=False,
            indent=4
        )