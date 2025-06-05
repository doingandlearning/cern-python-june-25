temps = []
with open("file.log") as file:
    for line in file:
        date, temp = line.strip().split(" - ")
        temps.append(int(temp))

print(temps)
print(f"Max: {max(temps)}")
print(f"Min: {min(temps)}")
print(f"Avg: {sum(temps)/len(temps)}")