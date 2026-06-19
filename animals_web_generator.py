import json
import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")


def load_data_from_animals_api(animal):
    response = requests.get(f"https://api.api-ninjas.com/v1/animals?X-Api-Key={API_KEY}&name={animal}")
    return response.json()


def read_html_file(file_path):
    """ Reads a HTML file """
    with open(file_path, "r") as handle:
        return handle.read()


def serialize_animal(animal_info):
    """ Serializes following information about each animal if existing:\n
        - name
        - diet
        - location (first one in the list)
        - type """
    animal_info_str = '<li class="cards__item">'
    if "name" in animal_info.keys():
        name = f'<div class="card__title">{animal_info["name"]}</div>'
        animal_info_str += name
    animal_info_str += '<p class="card__text">'
    if "diet" in animal_info["characteristics"].keys():
        diet = f'<strong>Diet:</strong> {animal_info["characteristics"]["diet"]}<br/>'
        animal_info_str += diet
    if "locations" in animal_info.keys():
        location = f'<strong>Location:</strong> {animal_info['locations'][0]}<br/>'
        animal_info_str += location
    if "type" in animal_info["characteristics"].keys():
        animal_type = f'<strong>Type:</strong> {animal_info['characteristics']['type']}<br/>'
        animal_info_str += animal_type
    animal_info_str += '</p>'
    animal_info_str += '</li>'
    return animal_info_str


def get_all_animal_info_as_string(file_path):
    """ Serializes following information about each animal if existing to html ul:\n
        - name
        - diet
        - location (first one in the list)
        - type """
    animals_info = load_data_from_animals_api("fox")
    animals_info_str = ''
    for animal_info in animals_info:
        animals_info_str += serialize_animal(animal_info)
    return animals_info_str


def main():
    html_template = read_html_file("animals_template.html")
    animals_info = get_all_animal_info_as_string("animals_data.json")
    html_output = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_info)
    with open("animals.html", "w") as handle:
        handle.write(html_output)

if __name__ == "__main__":
    main()

