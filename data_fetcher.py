import requests


def fetch_data(animal_name):

    url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"

    headers = {
        "X-Api-Key": "YOUR_API_KEY"
    }

    response = requests.get(url, headers=headers)

    return response.json()