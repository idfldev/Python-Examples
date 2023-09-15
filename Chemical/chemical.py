
import re
import requests


import requests

def check_reach_svch(cas_number):
    """
    Function to check if a chemical with the given CAS number is on the REACH SVHC list.

    Args:
        cas_number (str): The CAS number to be checked.

    Returns:
        bool: True if the chemical is on the REACH SVHC list, False otherwise.
    """
    url = f"https://pubchem.ncbi.nlm.nih.gov/#query={cas_number}"
    response = requests.get(url)
    try:
        data = response.json()
    except:
        print(f"Failed to retrieve REACH SVHC list for CAS number {cas_number}.")
        return None

    if "entries" in data and data["entries"]:
        return True
    else:
        return False

# Example usage
cas_number = "50-78-2"
result = check_reach_svch(cas_number)
if result is None:
    print("Failed to retrieve REACH SVHC list.")
elif result:
    print(f"The chemical with CAS number {cas_number} is on the REACH SVHC list.")
else:
    print(f"The chemical with CAS number {cas_number} is not on the REACH SVHC list.")


def check_cas_number(cas_number):
    """
    Function to check the validity of a CAS number.

    Args:
        cas_number (str): The CAS number to be checked.

    Returns:
        bool: True if the CAS number is valid, False otherwise.
    """
    pattern = r'^\d{2,7}-\d{2}-\d$'  # Regular expression pattern for CAS numbers
    if re.match(pattern, cas_number):
        return True
    else:
        return False

# Example usage

# cas_number = input("enter CAS #: ")
# check_reach_svch(cas_number)


# while True:
#     cas_number = input("enter CAS #: ")
#     if check_cas_number(cas_number):
#         print(f"{cas_number} is a valid CAS number.")
#     else:
#         print(f"{cas_number} is not a valid CAS number.")


# https://www.echa.europa.eu/web/guest/search-for-chemicals?p_p_id=disssimplesearch_WAR_disssearchportlet&p_p_lifecycle=0&_disssimplesearch_WAR_disssearchportlet_searchOccurred=true&_disssimplesearch_WAR_disssearchportlet_sessionCriteriaId=dissSimpleSearchSessionParam101401681977958222