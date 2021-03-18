data = {}

with open("currency_acronym_list.csv") as rf:
    for line in rf:
        currency, full_acr = line[0:3], line[4:].replace("\n", "")
        data[full_acr] = currency
