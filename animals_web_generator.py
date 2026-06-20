from data_fetcher import fetch_data


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


def get_all_animal_info_as_string(animal):
    """ Serializes following information about each animal if existing to html ul:\n
        - name
        - diet
        - location (first one in the list)
        - type """
    animals_info = fetch_data(animal)
    if not animals_info:
        return f"<h2>Your animal „{animal}“ doesn't exist.</h2>"
    animals_info_str = ''
    for animal_info in animals_info:
        animals_info_str += serialize_animal(animal_info)
    return animals_info_str


def main():
    html_template = read_html_file("animals_template.html")
    animal = input("Enter a name of an animal: ")
    animals_info = get_all_animal_info_as_string(animal)
    html_output = html_template.replace("__REPLACE_ANIMALS_INFO__", animals_info)
    with open("animals.html", "w") as handle:
        handle.write(html_output)


if __name__ == "__main__":
    main()

