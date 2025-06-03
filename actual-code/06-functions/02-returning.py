# def sum(a,b):
#     return a + b
#
# print(sum(2,3))
# print(sum(4,5))
# print(f"5 + 6 = {sum(5,6)}")
#
# result = sum(5,6)
# print(result)

def stats(list_of_numbers):
    """
    Calculates the basic statistics of a list of numbers
    :param list_of_numbers: Should be a list of numbers
    :return: A dict with min, max, avg
    """
    min_ = min(list_of_numbers)
    max_ = max(list_of_numbers)
    avg_ = sum(list_of_numbers) / len(list_of_numbers)

    return {"min":min_, "max":max_, "avg":avg_}

print(stats([4,6,5.5,10,-4]))