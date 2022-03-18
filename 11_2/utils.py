import json


def load_candidates(path):
    with open(path, encoding="utf-8") as file:
        data = json.load(file)
    return data

