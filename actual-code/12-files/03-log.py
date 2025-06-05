from datetime import datetime

file = open("file.log", "a")

while True:
    value = input("What's the temp? ")
    file.write(f"[{datetime.now().strftime()}] - {value}\n")

    go_again = input("Continue? ")
    if go_again == "no":
        break

file.close()
# syntanic sugar
# with open("file.log", "a") as file:
#     while True:
#         value = input("What's the temp? ")
#         file.write(f"[] - {value}\n")
#
#         go_again = input("Continue? ")
#         if go_again == "no":
#             break