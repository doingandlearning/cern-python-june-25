data = [4.4, 10.6,18.7, 3, 5]

new_list = []

for temp in data:
    if temp > 10:
        new_list.append(temp)

print(new_list)

def greater_than_ten(value):
    return value > 10

def greater_than_eleven(value):
    return value > 11

print(list(filter(greater_than_eleven, data)))
print(list(filter(lambda value: value < 10, data)))

list_of_records = [
    {"name": "Kevin", "home": "Belfast"},
    {"name": "Michal", "home": "Krakow"},
    {"name": "Aymeric", "home": "Peru"},
    {"name": "Dimitar", "home": "Bulgaria"}
]

list_of_records.sort(key=lambda record: record["home"])

print(list_of_records)
