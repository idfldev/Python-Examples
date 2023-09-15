
# import pubchempy as pcp
#
# cas_number = '50-78-2'  # example CAS number for acetaminophen
#
# try:
#     results = pcp.get_compounds(cas_number, 'cas')
#     if results:
#         compound = results[0]
#         print(f"Chemical name for CAS {cas_number} is: {compound.iupac_name}")
#     else:
#         print(f"No results found for CAS number {cas_number}")
# except pcp.PubChemHTTPError as e:
#     print(f"PubChemHTTPError: {e.msg}")

import requests
from bs4 import BeautifulSoup

# Define the URL to scrape
url = 'https://en.wikipedia.org/wiki/Web_scraping'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all the links on the page
    links = soup.find_all('a')

    # Print the text and href attribute of each link
    for link in links:
        print(f"Text: {link.text} \t\t Href: {link.get('href')}")
else:
    print(f"Request failed with status code {response.status_code}")
