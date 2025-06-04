class Person:
    species = "Homosapien"
    def __init__(self, name, location, age):
        self.name = name
        self.location = location
        self.age = age

    def __str__(self):
        return f"{self.name}[{self.species}] is in {self.location}"

    def __len__(self):
        return len(self.name)

    def say_hello(self):
        print(f"Hi, I'm {self.name} - nice to meet you!")

    def birthday(self):
        print(f"Hi, {self.name}, you were {self.age} - Happy birthday!")
        self.age += 1
        print(f"Now you are {self.age}")




person = Person("Aymeric", "Peru", 102)  # instantiates the class -> creates an object from the class
person2 = Person("Ethan", "Belfast", 12)

print(person)
print(dir(person))
print(len(person))
print(person2)  # Protocols

result1 = {"experiment": "LHC", "date": "today", "temperature": 12}

class Result:
    def __init__(self, experiment, date, temperature):
        self.experiment = experiment
        self.date = date
        self.temperature = temperature

# result2 = Result("LHC", "today", -

person.say_hello()
person2.say_hello()

person.birthday()
person2.birthday()

print(str.__doc__)