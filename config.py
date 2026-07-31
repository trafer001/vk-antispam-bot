import json


def load_groups():
    with open("groups.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    return data.get("groups", [])