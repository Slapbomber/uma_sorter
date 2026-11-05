import csv
import os
from char_details import Uma

OUTPUT_DIR = "uma_csvs"

def create_uma_csv(umas, stat_headers, filename="characters.csv"):

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    filepath = os.path.join(OUTPUT_DIR, filename)

    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(Uma.get_headers(stat_headers))

        for uma in umas:
            writer.writerows(uma.to_rows())

    print(f"saved {len(umas)} characters to {filepath}")