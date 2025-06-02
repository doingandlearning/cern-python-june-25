user_input = input("Give me a number: ")

while not user_input.isdigit():
    print("Whoops! You gave me some non-digits, try again")
    user_input = input("Give me a number: ")

user_input = int(user_input)

print(f"{user_input + 1} is one more than your number.")