import requests
from bs4 import BeautifulSoup

# # Define the URL to scrape
# url = 'https://pubchem.ncbi.nlm.nih.gov/#query=108-78-1'
#
# # Send a GET request to the URL
# response = requests.get(url)
#
# # Check if the request was successful
# if response.status_code == 200:
#     # Parse the HTML content using BeautifulSoup
#     soup = BeautifulSoup(response.content, 'html.parser')
#
#     # Find the search results container
#     results = soup.find('div', {'id': 'result_list_container'})
#
#     # Find the first search result item
#     item = results.find('div', {'class': 'search-result'})
#
#     # Extract the compound name
#     name = item.find('div', {'class': 'name'}).a.text.strip()
#     print(f"Compound Name: {name}")
#
#     # Extract the PubChem CID
#     cid = item.find('div', {'class': 'cid'}).text.strip()
#     print(f"PubChem CID: {cid}")
# else:
#     print(f"Request failed with status code {response.status_code}")
#



# Define the URL to scrape
url = 'https://pubchem.ncbi.nlm.nih.gov/#query=108-78-1'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the search results container
    results = soup.find('div', {'id': 'result_list_container'})
    
    # Find the first search result item
    item = results.find('div', {'class': 'search-result'})

    # Extract the compound name
    name = item.find('div', {'class': 'name'}).a.text.strip()
    print(f"Compound Name: {name}")

    # Extract the PubChem CID
    cid = item.find('div', {'class': 'cid'}).text.strip()
    print(f"PubChem CID: {cid}")
else:
    print(f"Request failed with status code {response.status_code}")
