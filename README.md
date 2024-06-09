# Web Scraping Script

This Python script scrapes unique links from a given website URL and saves them to both a text file and an Excel file.

## Installation

1. Clone this repository to your local machine.
2. Navigate to the repository directory.
3. Install the required dependencies using `pip` and the provided `requirements.txt` file:

```bash
pip install -r requirements.txt

Usage

    Run the script using Python.
    When prompted, enter the URL of the website you want to scrape.
    Enter the desired output file name (without extension) when prompted.

Code Explanation

The script utilizes the requests library to send a GET request to the specified URL and retrieve the HTML content. It then uses BeautifulSoup to parse the HTML and find all <a> tags (links). External links are filtered out, and unique links are stored in a set.
The user is prompted to specify the output file name, and the unique links are saved to both a text file (.txt) and an Excel file (.xlsx)
