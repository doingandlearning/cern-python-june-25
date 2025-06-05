import csv
import datetime
# comma seperated values

# location,date,temperature
# Meyrin,2025-06-05,14

temps = [
    ("Accra", datetime.date.today(), 24),
    ("Adelaide", datetime.date.today(), 14),
    ("Hanoi", datetime.date.today(), 33),
    ("Oslo", datetime.date.today(), 11),
]

with open("temps.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["location","date","temperature"])
    for temp in temps:
        writer.writerow(temp)



