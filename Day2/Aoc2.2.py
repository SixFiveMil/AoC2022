win = {
    "A":"Y",
    "B":"Z",
    "C":"X"
}
loss = {
    "A":"Z",
    "B":"X",
    "C":"Y"
}
tie = {
    "A":"X",
    "B":"Y",
    "C":"Z"
}
score= {
    "X":1,
    "Y":2,
    "Z":3,
    "A":1,
    "B":2,
    "C":3
}

count=0

f = open("Day2/input","r")
for line in f.readlines():
    play = line.split()
    opp = play[0]
    sel = play[1]
    #Check for in +6
    if sel == "Z":
        count += 6 + score[win[opp]]
    #Check if tie
    elif sel == "Y":
        count += 3 + score[tie[opp]]
    else:
        count += score[loss[opp]]

print(count)