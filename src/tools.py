import json
import requests
import os
from bs4 import BeautifulSoup


def search(query):
    url = 'https://google.serper.dev/search'

    payload = json.dumps({'q': query})
    headers = {
        'X-API-KEY': os.getenv('SERPER_API_KEY'),
        'Content-Type': 'application/json',
    }

    response = requests.request('POST', url, headers=headers, data=payload)

    return response.json()


def fetch(url: str) -> str:
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup.get_text()
    else:
        print(f'Request failed with status code {response.status_code}')
