from get_page_info import get_page, get_char_cards
from create_csv import create_uma_csv
import argparse

GRADE_ORDER = "ABCDEFG"
APTITUDE_GETTERS = {
    "turf": lambda uma: uma.track_aptitude.turf,
    "dirt": lambda uma: uma.track_aptitude.dirt,
    "sprint": lambda uma: uma.distance_aptitude.sprint,
    "mile": lambda uma: uma.distance_aptitude.mile,
    "medium": lambda uma: uma.distance_aptitude.medium,
    "long": lambda uma: uma.distance_aptitude.long,
    "front": lambda uma: uma.style_aptitude.front,
    "pace": lambda uma: uma.style_aptitude.pace,
    "late": lambda uma: uma.style_aptitude.late,
    "end": lambda uma: uma.style_aptitude.end,
}

def meets_minimum(actual_grade, minimum_grade):
    return GRADE_ORDER.index(actual_grade) <= GRADE_ORDER.index(minimum_grade)

def main():
    
    parser = argparse.ArgumentParser(description="Command line tool that scrapes umamusume character data from Uma.guide to convert into csv files")

    # List all characters
    parser.add_argument("--list-all", action="store_true", help="List names of all scraped characters, then exit")

    # Specify by name
    parser.add_argument("--name", nargs="+", help="Filter by one or more character names")

    # Filter by aptitude ranks
    parser.add_argument("--aptitude-type", choices=["dirt", "turf", "sprint", "mile", "medium", "long", "front", "pace", "late", "end"], 
                        help="Filter by specific aptitude category")
    parser.add_argument("--min-grade", default="B", help="Minimum grade to include (default is B)")

    args = parser.parse_args()

    # If no flags passed, show help and exit early
    if not any([args.list_all, args.name, args.aptitude_type]):
        parser.print_help()
        return

    # Scraping
    soup = get_page()
    umas, stat_headers = get_char_cards(soup)

    if args.list_all:
        for uma in umas:
            print(f"{uma.name} - {uma.title}")
        return # No CSV creation yet

    filtered_umas = umas
    
    if args.name:
        search_terms = [n.lower() for n in args.name]
        filtered_umas = [
            uma for uma in filtered_umas
            if any(term in uma.name.lower() for term in search_terms)
        ]

    if args.aptitude_type:
        get_grade = APTITUDE_GETTERS[args.aptitude_type]
        filtered_umas = [
            uma for uma in filtered_umas
            if meets_minimum(get_grade(uma), args.min_grade)
        ]

    create_uma_csv(filtered_umas, stat_headers)



if __name__ == "__main__":
    main()    