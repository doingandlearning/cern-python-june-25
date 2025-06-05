import csv

temps = []

class Reading:
    def __init__(self, reading):
        location, date, temp = reading
        self.location = location
        self.date = date
        self.temp = temp

    def __repr__(self):
        return f"Temperature in {self.location} on {self.date} is {self.temp} degrees celcius"

with open("temps.csv") as file:
    reader = csv.reader(file)

    headers = next(reader)  # to skip rows
    for row in reader:
        temps.append(Reading(row))

print(temps)