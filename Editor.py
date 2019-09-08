"""

Box of useful stuff

"""

import usefulBox as box


"""
Screen 1 is listing monsters + moves
Screen 2 is "edit monster x"
Screen 3 is "move x", applied to monster inherited from Screen 2
"""
file = input("File path? Please note that you only have one chance to type\nthis properly. Otherwise, you will have to restart.\n>>> ")
f = open(file, "r")
go = 1
monsters = []
index = -1
while go ==1:
    line = f.readline()
    if line[0] == "$":
        index += 1
        monsters.append([])
        monsters[index].append(line[1:len(line)-1])
        monsters[index].append([])
    elif line[0] == "@":
        monsters[index][1].append((line[1:len(line)-1]).split(";"))
    elif line[0] == "&":
        go = 0
        break
    else:
        print("Document error. Strange line involved. Line:\n" + str(line))
del index
del go
f.close()
del f
#print (monsters)

for monster in monsters:
    for move in monster[1]:
        move[1] = int(move[1])
        move[2] = int(move[2])

#print (monsters) #WORKS!!

def save(file):
    f = open(file, "w")
    #print("txt opened")
    for monster in monsters:
        f.write("$" + monster[0] + "\n")
        for move in monster[1]:
            f.write("@" + move[0] + ";" + str(move[1]) + ";" + str(move[2]) + "\n")
    f.write("&")
    f.close()

def screen1():
    index = 0
    for monster in monsters[1:len(monsters)]:
        index += 1
        print ("\nMonster " + str(index) + ": " + monster[0])
        for move in monster[1]:
            print ("	" + move[0] + "\n		" + str(move[1]) + " raw dmg, " + str(move[2]) + " lvl")
    del index

def screen2(mon):
    print (monsters[mon][0])
    for move in monsters[mon][1]:
        print ("    " + move[0] + "\n	    " + str(move[1]) + " raw dmg, " + str(move[2]) + " lvl")
    del mon

def screen3(mon, move):
#move cannot be zero.
    print ("\n" + monsters[mon][1][move][0] + "\n    " + str(monsters[mon][1][move][1]) + " raw dmg, " + str(monsters[mon][1][move][2]) + " lvl")
    del mon
    del move




screen = 1
cont = 1
while cont == 1:
    if screen == 1:
        screen1()
        inp = input(">>> ").lower()
        if "stop" in inp:
            cont = 0
            break
        elif "edit monster " in inp:
            #print (inp[13:len(inp)])
            inp = inp[13:len(inp)]
            again = 1
            while again == 1:
                try:
                    int(inp)
                except ValueError:
                    inp = input("Not a number!\n>>>edit monster ")
                    again = 1
                except:
                    inp = input("Some horrible accident occurred!\n>>>edit monster ")
                    again = 1
                else:
                    if int(inp)  > len(monsters) -1:
                        inp = input("Out of range!\n>>>edit monster ")
                        again = 1
                    else:
                        again = 0
                        break
            del again
            screen = 2
            cMon = int(inp)
        elif "add monster" in inp:
            monsters.append([])
            monsters[len(monsters) - 1].append(box.nameFormatter(input("Name?\n>>> ")))
            print("Monster with ID " + str(len(monsters)) + " automatically created.")
            monsters[len(monsters) - 1].append([["Tackle",6,0]])
            print ("Move 1 automatically created. Have fun with " + monsters[len(monsters) - 1][0] + "!")
            box.pause()
            #print(monsters)
        elif "del monster " in inp:
            inp = inp[12:len(inp)]
            again = 1
            while again == 1:
                try:
                    int(inp)
                except ValueError:
                    inp = input("Not a number!\n>>> del monster ")
                    again = 1
                except:
                    inp = input("Some horrible accident occurred!\n>>> del monster ")
                    again = 1
                else:
                    if int(inp) > len(monsters) -1:
                        inp = input("Out of range!\n>>> del monster ")
                        again = 1
                    else:
                        again = 0
                        break
            del again
            print(monsters[int(inp)][0] + " deleted!")
            monsters.pop(int(inp))
            box.pause()
            del inp
        elif inp == "save":
            save(file)
            print("Saved!")
            box.pause()
        #del inp

    if screen == 2:
        screen2(cMon)
        inp = input(">>> ").lower()
        if "stop" in inp:
            cont = 0
            break
        elif "back" in inp:
            screen = 1
        elif "name " in inp:
            monsters[cMon][0] = box.nameFormatter(inp[5:len(inp)])
        elif "move " in inp[0:6]:
            inp = inp[5:len(inp)]
            again = 1
            while again == 1:
                try:
                    int(inp)
                except ValueError:
                    inp = input("Not a number!\n>>>move ")
                    again = 1
                except:
                    inp = input("Some horrible accident occurred!\n>>>move ")
                    again = 1
                else:
                    if int(inp) > len(monsters[cMon][1]):
                        inp = input("Out of range!\n>>>move ")
                        again = 1
                    else:
                        again = 0
                        break
            del again
            screen = 3
            cMove = int(inp) -1
        elif "del move " in inp:
            inp = inp[9:len(inp)]
            print (inp)
            again = 1
            while again == 1:
                try:
                    int(inp)
                except ValueError:
                    inp = input("Not a number!\n>>> del move ")
                    again = 1
                except:
                    inp = input("Some horrible accident occurred!\n>>> del move ")
                    again = 1
                else:
                    if int(inp) > len(monsters[cMon][1]):
                        inp = input("Out of range!\n>>> del move ")
                        again = 1
                    else:
                        again = 0
                        break
            del again
            inp = int(inp) - 1
            print(monsters[cMon][1][inp][0] + " deleted!")
            monsters[cMon][1].pop(inp)
            box.pause()
            #del inp
        elif "add move" in inp:
            monsters[cMon][1].append([])
            monsters[cMon][1][len(monsters[cMon][1]) -1].append(box.nameFormatter(input("Name?\n>>> ")))
            inp = input("Damage?\n>>> ")
            again = 1
            while again == 1:
                try:
                    int(inp)
                except ValueError:
                    inp = input("Not a number!\nDamage?\n>>> ")
                    again = 1
                except:
                    inp = input("Some horrible accident occurred!\nDamage?\n>>> ")
                    again = 1
                else:
                    monsters[cMon][1][len(monsters[cMon][1]) -1].append(int(inp))
                    again = 0
                    break

            inp = input("Level?\n>>> ")
            again = 1
            while again == 1:
                try:
                    int(inp)
                except ValueError:
                    inp = input("Not a number!\nLevel?\n>>> ")
                    again = 1
                except:
                    inp = input("Some horrible accident occurred!\nLevel?\n>>> ")
                    again = 1
                else:
                    monsters[cMon][1][len(monsters[cMon][1]) -1].append(int(inp))
                    again = 0
                    break
            del again
            
        del inp

    if screen == 3:
        screen3(cMon, cMove)
        inp = input(">>> ").lower()
        if "stop" in inp:
            cont = 0
            break
        elif "back" in inp:
            screen = 2
        elif "name " in inp:
            monsters[cMon][1][cMove][0] = box.nameFormatter(inp[5:len(inp)])
        elif "dmg " in inp:
            inp = inp[4:len(inp)]
            again = 1
            while again == 1:
                try:
                    int(inp)
                except ValueError:
                    inp = input("Not a number!\n>>>move ")
                    again = 1
                except:
                    inp = input("Some horrible accident occurred!\n>>>move ")
                    again = 1
                else:
                    monsters[cMon][1][cMove][1] = int(inp)
                    again = 0
                    break
            del again
        elif "lvl " in inp:
            inp = inp[4:len(inp)]
            again = 1
            while again == 1:
                try:
                    int(inp)
                except ValueError:
                    inp = input("Not a number!\n>>>move ")
                    again = 1
                except:
                    inp = input("Some horrible accident occurred!\n>>>move ")
                    again = 1
                else:
                    monsters[cMon][1][cMove][2] = int(inp)
                    again = 0
                    break
            del again
        del inp




"""
inp == inp("")
if "name " in inp:
    monsters[cMon][0] = inp[5:len(inp)]
"""



















