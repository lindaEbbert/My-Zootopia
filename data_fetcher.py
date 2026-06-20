import requests
from dotenv import load_dotenv
import os
load_dotenv()
API_KEY = os.getenv("API_KEY")


def fetch_data(animal_name):
    """Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
    'name': ...,
    'taxonomy': {
      ...
    },
    'locations': [
      ...
    ],
    'characteristics': {
      ...
    }
    },
    """
    response = requests.get(f"https://api.api-ninjas.com/v1/animals?X-Api-Key={API_KEY}&name={animal_name}")
    return response.json()