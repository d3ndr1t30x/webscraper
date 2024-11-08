import requests
from bs4 import BeautifulSoup
import pandas as pd

# Prompt the user for the URL to scrape
website_url = input("Enter the URL to scrape: ")

# Send a GET request to the website and get the HTML content
response = requests.get(website_url)
html_content = response.content

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Find all <a> tags (links) in the HTML
links = soup.find_all("a")

# Use a set to store unique links
unique_links = set()

# Iterate through links and add unique ones to the set
for link in links:
    href = link.get("href")
    if href and href.startswith("http"):  # To filter out external links
        unique_links.add(href)

# Prompt the user for the output file name
output_filename = input("Enter the output file name (without extension): ")

# Append relevant extensions to the file name
text_output_filename = output_filename + ".txt"
excel_output_filename = output_filename + ".xlsx"

# Extract and save the unique links to the text file
with open(text_output_filename, "w") as text_output_file:
    for href in unique_links:
        text_output_file.write(href + "\n")

print("Scraped links saved to", text_output_filename)

# Create a DataFrame for the unique links and save to an Excel file
data = {"Links": list(unique_links)}
df = pd.DataFrame(data)
df.to_excel(excel_output_filename, index=False)

print("Scraped links saved to", excel_output_filename)
