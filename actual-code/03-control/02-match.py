user_colour = input("What is your favourite colour? ").lower()

print("Start of program")

match user_colour:
    case "green":  # equivalent to user_colour == green
        print("You must like grass and Ireland.")
    case "blue":
        print("You must like the sea and the sky.")
    case _:  # default case/fallback
        print("That's a nice colour!")

print("End of program")