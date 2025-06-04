class CERNLHCError(Exception):
    pass

try:
    raise CERNLHCError()
except CERNLHCError:
    print("Something went wrong")



def run_and_print(function, message):
    print("About to run the function")
    print(message)
    function()
    print("Ran the function")


def important_function():
    print("Very important work going on")

run_and_print(important_function, "Some message")