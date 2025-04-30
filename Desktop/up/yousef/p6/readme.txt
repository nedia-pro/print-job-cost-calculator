# Book Scraper 📚

Un petit script Python pour extraire les titres, prix et liens des livres depuis [books.toscrape.com](http://books.toscrape.com).

## Usage

1. Clone the repository.
2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the scraper:
    ```bash
    python scraper.py
    ```

This script will create a `books.csv` file with the extracted data.

## Dependencies

- `requests`
- `beautifulsoup4`
