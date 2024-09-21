import json
import os

from app.data import list_files

def open_file(path: str = list_files.ANIMALS) -> list:

    if not os.path.exists(path):
        with open(path, "w") as fh:
            json.dump([], fh)

    with open(path, "r", encoding="utf-8") as file:
        animals = json.load(file)

    return animals