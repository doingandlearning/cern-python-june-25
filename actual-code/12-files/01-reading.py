file = open("test.txt")

print(file.read())  # the whole contents as a string!
file.seek(0)

lines = file.readlines()

for line in lines:
    print(line.strip())

file.seek(0)

line = file.readline()

while line:
    print(line.strip())
    line = file.readline()

file.close()
