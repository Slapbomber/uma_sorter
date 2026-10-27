from get_page_info import get_page, get_char_cards


def main():
    
    print("Fetching index...")
    soup = get_page()
   

    print("Scraping character details...")
    umas = get_char_cards(soup)

   

    print(f"\nSuccessfully scraped {len(umas)} characters!\n")
    
    for uma in umas:
        print("Uma data:", uma.to_list())
        print("-" * 20)






if __name__ == "__main__":
    main()    