number_to_skip = int(input("Give me a number: "))

for number in range(0,10):
    if number == number_to_skip:
        continue
    print(f"Processing {number}.", "....", end="\n")

# for number in range(0,10):
#     if number != number_to_skip:
#         print(f"Processing {number}.")
#     else:
#         continue
