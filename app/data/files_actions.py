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


def save_file(file: list, path: str = list_files.ANIMALS):
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(file, fh, indent=4, ensure_ascii=False)

    
def del_animal(animal):
    animals = open_file()
    animals.remove(animal)
    save_file(animals)

    return f"Тваринку '{animal}' видалено"


def animal_cured(animal, path: str = list_files.ANIMALS_CURED) -> str:
    del_animal(animal)

    animal_cured = open_file(path)
    animal_cured.append(animal)
    save_file(animal_cured, path)

    return f"Тваринку '{animal}' вилікувано."