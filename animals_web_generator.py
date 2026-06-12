import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def read_html_file(file_path):
    """ Reads a HTML file """
    with open(file_path, "r") as handle:
        return handle.read()


def get_all_animal_info_as_string(file_path):
    """ Prints following information about each animal if existing:\n
        - name
        - diet
        - location (first one in the list)
        - type """
    animals_info = load_data(file_path)
    animals_info_str = ""
    for animal_info in animals_info:
        if "name" in animal_info.keys():
            name = f"Name: {animal_info["name"]}\n"
            animals_info_str += name
        if "diet" in animal_info["characteristics"].keys():
            diet = f"Diet: {animal_info["characteristics"]["diet"]}\n"
            animals_info_str += diet
        if "locations" in animal_info.keys():
            location = f"Location: {animal_info['locations'][0]}\n"
            animals_info_str += location
        if "type" in animal_info["characteristics"].keys():
            animal_type = f"Type: {animal_info['characteristics']['type']}\n"
            animals_info_str += animal_type
        animals_info_str += "\n"
    return animals_info_str


def main():
    html_template = read_html_file("animals_template.html")
    animals_info = get_all_animal_info_as_string("animals_data.json")
    html_output = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_info)
    with open("animals.html", "w") as handle:
        handle.write(html_output)

if __name__ == "__main__":
    main()

