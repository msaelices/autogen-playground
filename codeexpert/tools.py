import json
import requests


def search(query):
    url = 'https://google.serper.dev/search'

    payload = json.dumps({
        'q': query
    })
    headers = {
        'X-API-KEY': 'ab179d0f00ae0bafe47f77e09e62b9f53b3f281d',
        'Content-Type': 'application/json'
    }

    response = requests.request('POST', url, headers=headers, data=payload)

    return response.json()