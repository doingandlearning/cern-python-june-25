try:
    with open("test") as file:
        print(file.read())
except FileNotFoundError:
    print("Whoops! Can't find the file!")