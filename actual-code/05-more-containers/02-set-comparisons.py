s1 = {'apple', 'orange', 'banana'}
s2 = {'grapefruit', 'lime', 'banana'}

print("Union:")
print(s1 | s2)
print(s1.union(s2))

print("intersection")
print(s1 & s2)
print(s1.intersection(s2))

print("difference")
print(s1 - s2)
print(s1.difference(s2))

print("symmetric difference")
print(s1 ^ s2)
print(s1.symmetric_difference(s2))


list_of_things = ["apple", "apple", "banana", "banana"]
unique_items = list(set(list_of_things))
print(unique_items)

