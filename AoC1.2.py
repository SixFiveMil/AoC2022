totals=[]
current = 0
n=3
max=0

f = open("Day2/input","r")
for line in f.readlines():
    line = line.rstrip("\n")
    if line == "":
        totals.append(current)
        current = 0
    else:
        current += int(line)

totals.sort(reverse=True)
for x in range(0,n):
    max += totals[x]

print(max)