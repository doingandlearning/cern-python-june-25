number_of_tries = 0
player_name = "Kevin"

# if/while/for

def handle_player_name():
    # Read any global variable
    # "Shadow" any global variable
    temp = 4
    global player_name
    print(f"Your username is {player_name}.")
    player_name = input("What's your new username?")
    def inner():
        temp = 7
        print(temp, "inner")
    inner()
    print(temp, "outer")

handle_player_name()
print(player_name)