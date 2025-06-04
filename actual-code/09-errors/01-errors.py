# import traceback
# try:
#     print("Hello")
#     # print(5/0)
#     int("THISISNOTANUMBER")
#     open("none-file")
#     raise UnicodeError()
# except ZeroDivisionError as error:
#     print("You tried to divide by zero - duh!")
# except ValueError as expection:
#     print("That can't be turned into an int.")
#     print(expection)
#     traceback.print_exc()
# except Exception as e:
#     print("Something unexpected went wrong.")
#     print(e)
#
#
# print("You tried to do something.")
#
#
# def test_with_file(filename):
#     try:
#         open(filename)
#     except FileNotFoundError:
#         test_with_file("working_file_name")
#
#


test_results = [1,2,"error", 4, 5, 6]


for result in test_results:
    try:
        print(int(result))
    except ValueError as e:
        print(f"Something with wrong with value: {result}")























