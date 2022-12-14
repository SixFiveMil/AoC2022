#base set asci leters with values being index + 1
import string
priorities = list(string.ascii_letters)
found=[]
final = 0
#Read file line by line
f = open("Day3/input","r")
for line in f.readlines():
    line = line.rstrip("\n")
    #Split each line into two equil strings
    firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]
    for c in firstpart:
        if secondpart.count(c) > 0:
            found.append(c)
            break
    
#
for c in found:
    final += priorities.index(c) + 1
print(final)
