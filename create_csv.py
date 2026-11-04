import csv
import os
from get_page_info import get_page, get_char_cards
from char_details import Uma

OUTPUT_DIR = "uma_csvs"

def create_uma_csv(filename="characters.csv"):

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    filepath = os.path.join(OUTPUT_DIR, filename)


    soup = get_page()
    umas, stat_headers = get_char_cards(soup)

    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(Uma.get_headers(stat_headers))

        for uma in umas:
            writer.writerows(uma.to_rows())