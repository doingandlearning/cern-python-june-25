
# if/while/for
temp = 2
def non_local_example():
    # Read any global variable
    # "Shadow" any global variable
    temp = 4
    def inner():
        nonlocal temp
        temp = 7
        print(temp, "inner")
    inner()
    print(temp, "outer")

print(temp, "before function")
non_local_example()
print(temp, "after function")