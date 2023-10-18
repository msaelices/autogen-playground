import json
import requests
import os
from typing import Type
from bs4 import BeautifulSoup
from langchain.tools import BaseTool
from pydantic import BaseModel, Field


class SearchSchema(BaseModel):
    query: str = Field(description='should be a search query')


class SearchTool(BaseTool):
    name = 'search'
    description = 'Use this tool when you need to search some information on the internet'
    search_url = 'https://google.serper.dev/search'
    args_schema: Type[BaseModel] = SearchSchema

    def _run(self, query: str):
        payload = json.dumps({'q': query})
        headers = {
            'X-API-KEY': os.getenv('SERPER_API_KEY'),
            'Content-Type': 'application/json',
        }
        response = requests.request('POST', self.search_url, headers=headers, data=payload)

        return response.json()


class FetchSchema(BaseModel):
    url: str = Field(description='URL to fetch')


class FetchTool(BaseTool):
    name = 'fetch'
    description = 'Use this tool when you need to fetch some website content based on URL'
    args_schema: Type[BaseModel] = FetchSchema

    def _run(self, url: str):
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            return soup.get_text()
        else:
            print(f'Request failed with status code {response.status_code}')


# ----- Tools --------------------------------

search_tool = SearchTool()
fetch_tool = FetchTool()
