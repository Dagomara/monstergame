def nameFormatter(string):
    string = string.strip()
    string = string.title()
    return string
print (nameFormatter(input("What is your name? ")))




f = open("mons.txt", "r")
go = 1
specienames = []
allAttacks = []
index = -1
signal = 0
while go == 1:
    line = f.readline()
    if line[0] == "$":
        signal = 1
        #print (line[1:len(line)-1] + " is a monster name")
        temp = line[1:len(line)-1]
        specienames.append(temp)
        del temp
    elif line[0] == "@":
        #print (line[1:len(line)-1] + "is a move of that monster")
        if signal == 1:
            index += 1
            allAttacks.append([])
        temp = line[1:len(line)-1]
        allAttacks[index].append(temp.split(";"))
        signal = 0
        del temp
    elif line[0] == "&":
        go = 0
        break
del line
f.close()
del f
print (allAttacks)
for move in allAttacks:
    for i in move:
        i[1] = int(i[1])
        i[2] = int(i[2])
print (allAttacks)














"""
f = open("mons.txt", "r")
go = 1
specienames = []
allAttacks = []
while go == 1:
    line = f.readline()
    if line[0] == "$":
        print (line[1:len(line)-1] + " is a monster name")
        temp = line[1:len(line)-1]
        specienames.append(temp)
        del temp
    elif line[0] == "@":
        print (line[1:len(line)-1] + "is a move of that monster")
        temp = line[1:len(line)-1]
        allAttacks.append(temp.split(";"))
        del temp
    elif line[0] == "&":
        go = 0
        break
del line
f.close()
del f

#print (specienames)
#print (allAttacks)
#specienames = f.readline()
#print (specienames)
#allAttacks = f.readline()
#print (allAttacks)
#t1 = f.readline()
#t2 = f.readline()
#f.close()
"""
