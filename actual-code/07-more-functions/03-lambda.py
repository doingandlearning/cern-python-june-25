def print_msg():
    print("Hello from def")

print_msg()

print_msg = lambda: print("Hello from lambda")

print_msg()

def custom_sum(first, second):
    return first + second

print(custom_sum(1,2), "def")

custom_sum = lambda first, second: first + second

print(custom_sum(1,2), "lambda")