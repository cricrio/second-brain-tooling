import re

import requests
from bs4 import BeautifulSoup


def fetch_metadata(url: str) -> dict[str, str]:
    """
    Fetch the page and retrieve the og tags

    return list((property: str, content:str))
    """
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    tags = {}
    for tag in soup.find_all(property=re.compile('^og')):
        tags[tag['property']] = tag['content']
    return tags
