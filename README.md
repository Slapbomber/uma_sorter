# Uma-Sorter

This is a practice project for a program that scrapes character info from [Uma.guide](https://uma.guide/characters/) and then sorts and converts it into CSV file spreadsheet.

## How to Get

Clone the repository:

```
    git clone <repository_url>
    cd <repository_directory>
```

## Dependencies

This project requires Python 3.8+ and the following packages:

- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/) — HTML parsing
- [playwright](https://playwright.dev/python/) — Headless browser automation for JavaScript-rendered pages

### Installation

```
    bash
    pip install beautifulsoup4 playwright
    playwright install
```

The rest of the dependencies (`csv`, `os`, `argparse`, `time`, `urllib.parse`) are part of Python's standard library and require no additional installation.

### How to Use

Avalaible commands:

- **--help or no input**: Lists all the available commands and what they do.
- **--list-all**: Lists the name and title of all scraped characters.
- **--name <name>**: Generate a CSV file containing characters matching the inputted name. This is not case sensitive and you can also input multiple names.
- **--aptitude-type <aptitude>**: Generate a CSV file containing characters matching selected aptitude. By adding --min-grade <grade> you can specify which aptitude ranks are included, this is by default set to grade "B".
