max = 0
current = 0
f = open("Day1/input","r")
for line in f.readlines():
    line = line.rstrip("\n")
    if line == "":
        if current > max:
            max = current
        current = 0
    else:
        current += int(line)
print(max)