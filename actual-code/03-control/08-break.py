number_to_search_for = int(input("What number do you want?"))

for number in range(0, 1000):
    print(f"Checking {number} ...")
    if number == number_to_search_for:
        print("Found it!")
        break

while True:
    user_input = input("Keep going? ")
    if user_input == "n":
        break