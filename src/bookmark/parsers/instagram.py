import re

import requests
from bs4 import BeautifulSoup


def instagram_parser(url: str) -> list[tuple[str, str]]:
    """
    Fetch the page and retrieve the og tags

    return list((property: str, content:str))
    """
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    tags = []
    for tag in soup.find_all(property=re.compile('^og')):
        tags.append((tag['property'], tag['content']))
    return tags
