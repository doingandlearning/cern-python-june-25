# [1,2,3,4,5,6]
# {key:value}

cities = {
    "France": "Paris",
    "Poland": "Krakow",
    "India": "Dehli",
    "UK": ["London", "Edinburgh"]
}

print(cities["UK"][0])

cities["India"] = [cities["India"], "Chanai"]
print(cities)

#
# print(cities["France"])
# cities["UK"] = "Chester"
# cities["Bulgaria"] = "Sofia"
# # print(cities["Switzerland"])
# print(cities.get("India", "City not found"))
# print(cities.get("Switzerland", "City not found"))
# print(cities.setdefault("Switzerland", "Bern"))
# print(cities.setdefault("India", "Chanai"))
# print(cities)
#

print("UK" in cities)
print("Krakow" in cities)

print(cities.keys())
print(cities.values())
print(cities.items())


person = ("Kevin", "Belfast", 2)

name, city, no_of_children = person

print(f"{name} lives in {city} and is father to {no_of_children} children.")



for country, city in cities.items():
    print(f"{country} has a city or cities called {city}")



