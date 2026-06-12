import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def print_all_animal_info(file_path):
    """ Prints following information about each animal if existing:\n
        - name
        - diet
        - location (first one in the list)
        - type """
    animals_info = load_data(file_path)
    for animal_info in animals_info:
        if "name" in animal_info.keys():
            print(f"Name: {animal_info["name"]}")
        if "diet" in animal_info["characteristics"].keys():
            print(f"Diet: {animal_info["characteristics"]["diet"]}")
        if "locations" in animal_info.keys():
            print(f"Location: {animal_info['locations'][0]}")
        if "type" in animal_info["characteristics"].keys():
            print(f"Type: {animal_info['characteristics']['type']}")
        print()

