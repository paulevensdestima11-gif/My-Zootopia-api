import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = "https://api.api-ninjas.com/v1/animals"


def fetch_data(animal_name):
    """
     Fetches the animals data for the animal 'animal_name'.
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

    url = f"{API_URL}?name={animal_name}"

    headers = {
        "X-Api-Key": API_KEY
    }

    response = requests.get(url, headers=headers)

    return response.json()