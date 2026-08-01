import json


def load_json(file_name):

    with open(
        file_name,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def save_json(file_name, data):

    with open(
        file_name,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=4
        )