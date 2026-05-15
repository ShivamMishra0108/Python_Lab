countries = ("India", "China", "Brazil", "Cannada", "Germany")

# OPERATIONS/MODIFICATIONS IN TUPLE BY USING REFERENCE

temp = list(countries)   # converted tuple into list(temp)

temp.append("Russia")    # add new item
temp.pop(1)              # delete an item
temp[2] = "Spain"          # replace an item

countries = tuple(temp)    # converted list into tuple(countries)
print(countries)


country1 = ("India", "China", "Brazil")
country2 = ("Cannada", "Germany")

Country = country1 + country2
print(Country)