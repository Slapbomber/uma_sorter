import requests
import time
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from char_details import Uma, Stats, TrackAptitude, StyleAptitude, DistanceAptitude

BASE_URL = "https://uma.guide"

stat_names = ["speed", "stamina", "power", "guts", "wit"]
aptitude_ranks = ["A", "B", "C", "D", "E", "F", "G"]


def get_page():
    url = "https://uma.guide/characters/"
    response = requests.get(url)

    print("Status code:", response.status_code)
    response.raise_for_status()

    print("Success! Downloaded", len(response.text), "characters of HTML")

    soup = BeautifulSoup(response.content, "html.parser")

    return soup

def get_char_stats(detail_url, session):
    response = session.get(detail_url)
    response.raise_for_status()

    char_soup = BeautifulSoup(response.content, "html.parser")

    stat_grid = char_soup.find("div", class_="stat-grid")
    if not stat_grid:
        return None

    val_tags = stat_grid.find_all("div", class_="stat-grid_value")
    growth_tags = stat_grid.find_all("div", class_="stat-grid_growth")

    vals = [tag.get_text(strip=True) for tag in val_tags]
    growths = [tag.get_text(strip=True) for tag in growth_tags]

    stats = Stats(*vals, *growths)

    return stats

def get_char_cards(soup):

    char_grid_container = soup.find("div", class_="character-grid-container")
    char_grid = char_grid_container.find("div", class_="character-grid")
    cards = char_grid.find_all("a", class_="character-card")

    for card in cards:
        # png
        img_tag = card.find("img", class_="character-icon")
        img_url = img_tag.get("src") if img_tag else None
        if img_url and img_url.startswith("/"):
            img_url = f"https://uma.guide{img_url}"

        #name
        name = card.find("div", class_="character-name")
        name_text = name.get_text(strip=True) if name else "Unknown"

        #title
        title = card.find("div", class_="card-title")
        title_text = title.get_text(strip=True) if title else "Unknown"

        relative_link = card.get("href")
        detail_url = urljoin(BASE_URL, relative_link)

