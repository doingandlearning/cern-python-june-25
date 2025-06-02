empty_tuple = () # or tuple()

print(empty_tuple)
print(type(empty_tuple))

print(empty_tuple.count(13))
# print(empty_tuple.index(13)) - make sure it's there first!

name_tuple = ("Michal", "Aymeric", "Rahul", "Dimitar", 1471)

print(name_tuple[0])   # who is in position 0
print(name_tuple[1:])  # from 1 to the end
print(name_tuple[2:4]) # from 2 up to by not including 4
print(len(name_tuple))

print("Marc" in name_tuple)

for name in name_tuple:
    print(f"Hi {name}, nice to see you! Only 30 minutes til home :)")

color_tuple = ("green", "blue", "red", "yellow")

big_tuple = (name_tuple, color_tuple, (1,2,3), "Woohoo!")

print(big_tuple)

## Rahul!
print(big_tuple[0][2])