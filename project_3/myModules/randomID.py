import random
from datetime import date


def generateIdForm(audit_type):
    """
    # N => new customer
    # R => renew  audit plan
    # C => our customer but change another standard

    ex: June23Ne2n753fs
    """

    today = date.today()
    current_date = today.strftime("%b%y")

    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
    password = ""
    len_pass = random.randrange(6, 12)
    for i in range(len_pass):
        password += random.choice(characters)

    id_url = current_date + audit_type.upper() + password

    return id_url
    






# permiss = generateIdForm("n")
# count = f"{permiss},{permiss},{permiss},{permiss}"
# print(count)
# count_lst = count.split(",")
# print(count_lst)
# print(len(count_lst))


# while True:
#     appilcation_type = input("Enter audit type: ")
#     print(generateIdForm(appilcation_type))
#     if appilcation_type.lower() == "stop":
#         break
