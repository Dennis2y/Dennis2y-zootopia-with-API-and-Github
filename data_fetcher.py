# data_fetcher.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

def fetch_data(animal_name):
    """
    Fetches the animal data from the API based on the name.
    Returns a list of animals (dictionaries) or an empty list if not found.
    """
    url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
    headers = {'X-Api-Key': API_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return []  # Empty list = no animals found or error
