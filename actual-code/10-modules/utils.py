"""
This is a utility module
- what's in here?
- what do you need to know?
- 3rd party libraries that it works ...
"""
import os

print(os.cpu_count())
print(os.name)
print(os.getgid())


def printer(some_object):
    print("I am the printer function")
    print(some_object)
    print("Did I do okay?")

class Shape:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"I am a Shape of name {self.name}"

default_shape = Shape("rhombus")

def main():
    print("Hello, I am the utils module!")
    print(f"My name is {__name__}")

if __name__ == "__main__":
    main()