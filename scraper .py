import requests
from bs4 import BeautifulSoup
import pandas as pd

# Replace this with the URL of the website you want to scrape
website_url = "https://example.com/architectural-firms"

# Send a GET request to the website and get the HTML content
response = requests.get(website_url)
html_content = response.content

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Find all <a> tags (links) in the HTML
links = soup.find_all("a")

# Prompt the user for the output file name
output_filename = input("Enter the output file name (without extension): ")

# Append relevant extensions to the file name
text_output_filename = output_filename + ".txt"
excel_output_filename = output_filename + ".xlsx"

# Extract and save the href attribute of each link to the text file
with open(text_output_filename, "w") as text_output_file:
    for link in links:
        href = link.get("href")
        if href and href.startswith("http"):  # To filter out external links
            text_output_file.write(href + "\n")

print("Scraped links saved to", text_output_filename)

# Create a DataFrame for the links and save to an Excel file
data = {"Links": [link.get("href") for link in links if link.get("href") and link.get("href").startswith("http")]}
df = pd.DataFrame(data)
df.to_excel(excel_output_filename, index=False)

print("Scraped links saved to", excel_output_filename)
