import requests
from bs4 import BeautifulSoup


def crawl_data(url):
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    texts = []

    for element in soup.find_all(["p", "h1", "h2", "h3"]):
        text = element.get_text(" ", strip=True)

        if text:
            texts.append(text)

    return texts