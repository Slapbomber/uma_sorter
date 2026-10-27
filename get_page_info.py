import time
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from char_details import Uma, Stats, TrackAptitude, StyleAptitude, DistanceAptitude

BASE_URL = "https://uma.guide"


def get_page():
    url = "https://uma.guide/characters/"
    
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)

        page.wait_for_selector(".character-grid-container")

        html = page.content()
        browser.close()

    print("Success! Downloaded", len(html), "characters of HTML")

    soup = BeautifulSoup(html, "html.parser")

    return soup

def get_char_soup(detail_url, browser):
    page = browser.new_page()
    page.goto(detail_url)
    page.wait_for_selector(".char-hero__panel")
    html = page.content()
    page.close()
    
    char_soup = BeautifulSoup(html, "html.parser")
    return char_soup

def get_char_stats(char_soup):
    

    stat_grid = char_soup.find("div", class_="stat-grid")
    if not stat_grid:
        return None

    val_tags = stat_grid.find_all("div", class_="stat-grid__value")
    growth_tags = stat_grid.find_all("div", class_="stat-grid__growth")

    vals = [tag.get_text(strip=True) for tag in val_tags]
    growths = [tag.get_text(strip=True) for tag in growth_tags]

    stats = Stats(*vals, *growths)

    return stats

def get_char_aptitudes(char_soup):
    rows = char_soup.find_all("div", class_="apt-row")

    all_row_grades = []
    for row in rows:
        badges = row.find_all("span", class_="apt-badge")
        grades = []

        for badge in badges:
            grade_tag = badge.find("b", class_="apt-badge__grade")
            grade = grade_tag.get_text(strip=True) if grade_tag else "N/A"
            grades.append(grade)

        all_row_grades.append(grades)

    track = TrackAptitude(*all_row_grades[0])
    distance = DistanceAptitude(*all_row_grades[1])
    style = StyleAptitude(*all_row_grades[2])

    return track, distance, style
        

def get_char_cards(soup):

    char_grid_container = soup.find("div", class_="character-grid-container")
    char_grid = char_grid_container.find("div", class_="character-grid")
    cards = char_grid.find_all("a", class_="character-card")

    with sync_playwright() as p:
        browser = p.chromium.launch()

        umas = []

        for card in cards[:2]:
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
            char_soup = get_char_soup(detail_url, browser)

            #stats
            stats = get_char_stats(char_soup)

            #aptitudes
            track, distance, style = get_char_aptitudes(char_soup)

            uma = Uma(img_url, name_text, title_text, stats, track, distance, style)
            umas.append(uma)

            time.sleep(0.5)

        browser.close()

    return umas

