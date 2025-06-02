import random

number_to_guess = random.randint(1,10)

number_of_guesses = 0
player_won = False

print(number_to_guess)
# for guess_number in range(0, number_of_guesses):
while number_of_guesses < 4:
    while True:
        guess = input("What's your guess?")
        if guess == "-1":
            guess = -1
            break


        if not guess.isdigit():
            continue
        guess = int(guess)
        break

    if guess == -1:
        print(f"Ssh The answer is {number_to_guess}")
        continue

    if guess == number_to_guess:
        print("Well done!")
        player_won = True
        break
    elif guess < number_to_guess:
        print("Too low, try again")
    else:
        print("Too high, try again")


    number_of_guesses += 1

if not player_won:
    print("Loser!")
else:
    print(f"You took {number_of_guesses + 1} tries.")