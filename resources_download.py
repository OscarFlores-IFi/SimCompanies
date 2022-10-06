


import requests
import json
import time

def general_data(full_list):
    producedFrom = [(i["amount"], i["resource"]["name"]) for i in full_list["producedFrom"]]
    neededFor = [i["name"] for i in full_list["neededFor"]]
    producedAnHour = full_list["producedAnHour"]
    baseSalary = full_list["baseSalary"]
    marketSaturation = full_list["marketSaturation"]
    retailModeling = full_list["retailModeling"]
    return {
            "producedFrom": producedFrom,
            "neededFor": neededFor,
            "producedAnHour": producedAnHour,
            "baseSalary": baseSalary,
            "marketSaturation": marketSaturation,
            "retailModeling": retailModeling}

def read_json(filename):
    with open(filename, 'r') as f:
        full_list = json.load(f)
    return full_list

def big_json(economy):
    # Economy = (0, 1, or 2); Recession, Normal or Boom
    big_dic = {}
    for i in range(146):
        filename = 'resources/prod_list/prod_list{}_{}.json'.format(economy,i)
        try:
            full_list = read_json(filename)
            big_dic[full_list["name"]] = general_data(full_list)
        except:
            pass

    with open('recession.json', 'w') as f:
        json.dump(big_dic, f)

############################# Download data ##############################

# resources_link = "https://www.simcompanies.com/api/v3/en/encyclopedia/resources/"
# full_list = requests.get(resources_link).json()
# with open('resources_list.json', 'w') as f:
#     json.dump(full_list, f)

# for j in range(3):
#     for i in range(145,146):
#         economy = j  # Boom=2, Normal=1, Recession=0
#         resource_link = "https://www.simcompanies.com/api/v3/en/encyclopedia/resources/{}/{}/".format(economy,i)
#         try:
#             resource = requests.get(resource_link).json()
#             with open('prod_list{}_{}.json'.format(economy,i), 'w') as f:
#                 json.dump(resource, f)
#             time.sleep(5)
#
#         except:
#             pass

################ Wrap important information into big json ################



big_json(1)
