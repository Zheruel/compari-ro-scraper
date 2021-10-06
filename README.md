# Compari.ro Scraper

Scraper for https://www.compari.ro.

### Initial setup
Install everything from requirements.txt using: `pip install -r /path/to/requirements.txt`.

### Main directory

`scrape_vendors.py`

Master script for running the scraping process.

### Models

`/models/vendor.py`

Model meant to represent the structure of saved vendor information.

### Web

`/web/vendor_scraping_controller`

Contains all the logic behind using HTTP requests to scrape all vendors on the website.

### IO Utils

`/io_utils/csv_exporter.py`

Contains logic for exporting scraped vendor information into a CSV file.

### Output

Scraped vendors get saved into a CSV file in `/output/scraped_vendors.csv`.
