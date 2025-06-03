list_of_squares = []

for number in range(1,101):
    if number % 2 == 0:
        list_of_squares.append(number ** 2)

print(list_of_squares)

list_of_squares = [number ** 2 for number in range(1,101) if number % 2 == 0]
print(list_of_squares)