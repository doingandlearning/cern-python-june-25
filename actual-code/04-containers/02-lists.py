empty_list = []

print(empty_list)
print(type(empty_list))

band_list = ["John", "Paul", "George", "Ringo"]
print(band_list[1])
print(band_list[1:])
print(band_list[:3])

band_list.append("Eloisa")
print(band_list)

band_list.extend(("Katie", "Marc", "Wilfried", "John"))
print(band_list)

band_list.insert(1, "Michal")
print(band_list)

band_list.remove("John")
print(band_list)

del band_list[3:5]
print(band_list)

third_person = band_list.pop(2)
print(third_person)
print(band_list)

for name in band_list:
    print(f"{name} is a great band member.")

print("Kevin" in band_list)

band_list[1] = "Kevin"

print(band_list)

for name in band_list:
    print(name.upper())