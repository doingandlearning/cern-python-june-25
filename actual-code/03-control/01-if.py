user_colour = input("What is your favourite colour? ").lower()

print("Start of program")

if user_colour == "green":
    print("You must like grass and Ireland.")
elif user_colour.startswith("g"):
    print("You must like the sea and the sky.")
else:
    print("That's a nice colour!")

print("End of program")