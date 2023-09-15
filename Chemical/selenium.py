from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Setting up the Chrome driver with Selenium
service = Service('/path/to/chromedriver')
options = Options()
options.headless = True
driver = webdriver.Chrome(service=service, options=options)

# Navigating to the PubChem website for the given CAS number
cas_number = '108-78-1'
url = 'https://pubchem.ncbi.nlm.nih.gov/#query=' + cas_number
driver.get(url)

# Extracting the chemical name from the page
chemical_name = driver.find_element_by_class_name('heading-1').text
print('Chemical Name:', chemical_name)

# Extracting the synonyms of the chemical from the page
synonyms_list = driver.find_element_by_id('synonyms')
synonyms = []
if synonyms_list:
    for synonym in synonyms_list.find_elements_by_tag_name('li'):
        synonyms.append(synonym.text)
print('Synonyms:', synonyms)

# Extracting the molecular formula of the chemical from the page
mol_formula = driver.find_element_by_css_selector('#chemical-and-physical-properties span#Molecular-Formula.value').text
print('Molecular Formula:', mol_formula)

# Extracting the molecular weight of the chemical from the page
mol_weight = driver.find_element_by_css_selector('#chemical-and-physical-properties span#Molecular-Weight.value').text
print('Molecular Weight:', mol_weight)

# Closing the driver
driver.quit()
