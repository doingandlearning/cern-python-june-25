my_string = "It's a string"
other_string = 'This is also a string'

print(my_string)
print(type(my_string))

print(len(my_string))

# overloaded operator
long_string = my_string + other_string + "and this one"

print(1 + 1)
print("1" + "1")

print("Hello, we are " + str(10) + "people in this room")

print(long_string.upper())
print(long_string.lower())

print(long_string.replace("string", "str"))
# long_string = long_string.replace("string", "str")

print(long_string.find("Kevin")) # zero indexed, -1 for not found

print(long_string == "Long string")
print(long_string != "Long string") # not equal to

print(long_string.startswith("It's"))

print(long_string[7])  # single character
print(long_string)
print(long_string[7:])  # from position 7 to position 10
print(long_string[7:15])
print(long_string[7:15:2])
print(len(long_string))
print(len(long_string.replace(" ", "")))



string_with_hashes = "This is a string # and this is the comment # and something else # this is the third"
print(string_with_hashes[string_with_hashes.find("#"):string_with_hashes.replace("#", "", 1).find("#")])


print(string_with_hashes.split("#"))