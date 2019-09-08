import random
import math
#base16nums = [1,2,3,4,5,6,7,8,9,0,"a","b","c","d","e","f"]

import context as out

"""
f = open("Saves/p1/p1.mon.txt", "r")
#specienames = f.readline()
#out.output (specienames)
#allAttacks = f.readline()
#out.output (allAttacks)
t1 = f.readline()
t2 = f.readline()
f.close()
"""
#specienames = ["null","Porygon","Pikachu","Sewaddle"]
#allAttacks = ["No moves available for monster \"null\"",[["Tackle",6,0],["SpecialMovePorygon",10,3]],[["Tackle",6,0],["SpecialMovePikachu",10,3]],[["Tackle",6,0],["SpecialMoveSewaddle",10,3]]]

"""

Box of useful stuff

"""

import usefulBox as box



"""

Specie name initializer

"""
monsFile =input("Monster filepath? Please note that you only have one chance to type\nthis properly. Otherwise, you will have to restart.\n>>> ")
#playerFile = out.feed("Player filepath? Please note that you only have one chance to type\nthis properly. Otherwise, you will have to restart.\n>>> ")
f = open(monsFile, "r")
go = 1
specienames = []
allAttacks = []
index = -1
signal = 0
while go == 1:
    line = f.readline()
    if line[0] == "$":
        signal = 1
        #out.output (line[1:len(line)-1] + " is a monster name")
        temp = line[1:len(line)-1]
        specienames.append(temp)
        del temp
    elif line[0] == "@":
        #out.output (line[1:len(line)-1] + "is a move of that monster")
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
del signal
del index
del line
f.close()
del f
for move in allAttacks:
    for i in move:
        i[1] = int(i[1])
        i[2] = int(i[2])
#out.output (allAttacks)

"""
if list(t1) == specienames:
    out.output ("t1 == specienames")
else:
    out.output ("net")
if list(t2) == allAttacks:
    out.output ("t2 == allAttacks")
else:
    out.output ("нет")
"""




"""
Game operation
"""
#Player and monster definitions



class monster():
    def __init__(self, nicked, givenSpecie):
        n = len(specienames) - 1
        #out.output (n)
        self.specie = random.randint(1,n)
        del n
        if (int(givenSpecie) != 0):
            self.specie = int(givenSpecie)
        self.xp = 0
        self.xpreq = 25
        self.level = 1
        self.speciename = specienames[self.specie]

        #naming conventions. On monster setup, you can do monster(1), 0, or "ask".
        #1 commands you to title your monster, 0 gives it no title, and "ask" asks the user.
        #I personally have the feeling that 1 will never be used, 0 will be for enemies, and
        #"ask" will be the most common, as it will be for every monster the user captures.
        if nicked == 1:
            out.output ("You got a new monster with specie ID " + str(self.specie) + ". It's a " + self.speciename + "!")
            self.nickname = box.nameFormatter(box.nameMaker(out.feed("Enter your monster's name. "), 15))
        elif nicked == "ask":
            littleTempString = "Do you wish to nickname your " +  self.speciename + "? "
            if ((out.feed(littleTempString)).lower() == "yes"):
                self.nickname = box.nameFormatter(box.nameMaker(out.feed("Enter your monster's name. "), 15))
                del littleTempString
            else:
                self.nickname = self.speciename
        else:
            self.nickname = self.speciename


        self.health = 25
        self.maxhealth = 25
        self.defense = 1
        self.attack = 1
        self.potion = 1
        self.availableMoves = allAttacks[self.specie]
        self.learnedMoves = []

        for i in self.availableMoves:
            if i[2] <= self.level:
                self.learnedMoves.append(i)
        #out.output ("Monster's learned moves are:" + self.learnedMoves)    #this is a debugging command for moves
        #out.output ("Monster's available moves are:" + self.availableMoves)    #this is a debugging command for moves
        """
        This was old, fragmented code that I had in the original plan.
            May use later for something though.

        def monstergen():
            genNum = random.choices(base16nums, k = 3)
            monsternum = str(monsterID) + genNum)
        """


    def rename(self):
        self.nickname = out.feed("Enter " + self.nickname + "'s new name.")

    def levelUp(self):
        self.level += 1
        self.xpreq *= 1.2
        self.xpreq += 2
        self.xpreq = math.floor(self.xpreq)
        self.attack += 0.08
        if (self.defense > 0.75):
            self.defense -= 0.005 #level 50 is max defense!
        self.maxhealth += math.ceil(0.1 * self.level**2)
        self.health = self.maxhealth #levelling up grants full heal!
        if (self.potion <5):
            self.potion += 0.04 #level 100 is max potion affinity!
        #move training automatica!
        for i in self.availableMoves:
            #out.output ("i is currently:" + str(i))    #this is a debugging command for moves
            if i[2] == self.level:
                #out.output ("i[2] is currently:" + str(i[2]))    #this is a debugging command for moves
                self.learnedMoves.append(i)
    def howManyMoves(self):
        x = 0
        for i in self.learnedMoves:
            x += 1
        #out.output ("x = " + str(x))
        return x
    def showMoves(self):
        out.output ("\nIndex: Move:           Raw Damage:")
        temp = 0
        for i in self.learnedMoves:
            temp +=1
            out.output (box.stringSolver(7, str(temp)) + box.stringSolver(15, i[0])+ " " + str(i[1]))
        del temp
    def showDetails(self):
        out.output ("            " + self.nickname + ":\n        Level " + str(self.level)  + " " + self.speciename + "\n        with " + str(self.health)  + "/" + str(self.maxhealth) + " HP\n        and " + str(self.xp) + "/" + str(self.xpreq) + " XP until next level.")
    def levelTo(self, desired):
        self.ttl = (desired - self.level) #ttl stands for "times to level."
        if (self.ttl >0):
            #that was purely a bs checker.
            while (self.level < desired):
                self.levelUp()
    def showBattleCard(self, enemy):
        if enemy:
            out.output ("\n\n======================================\n        Enemy " + self.nickname + ":\n    " + str(self.health) + "/" + str(self.maxhealth) + "HP\n    lvl " + str(self.level) + "\n    " + str(self.xp) + "/" + str(self.xpreq) + "XP\n======================================")
        else:
            out.output ("\n\n======================================\n        " + p1.name + "\'s " + self.nickname + ":\n    " + str(self.health) + "/" + str(self.maxhealth) + "HP\n    lvl " + str(self.level) + "\n    " + str(self.xp) + "/" + str(self.xpreq) + "XP\n======================================")
    def help(self):
        out.output("Vars:\n	xp\n	xpreq\n	level\n	speciename\n	health\n	nickname\n	maxhealth\n	defense\n	attack\n	potion\n	availableMoves\n	learnedMoves\n\nFunctions:\n	rename()\n	levelUp()\n	howManyMoves()\n	showMoves()\n	showDetails()\n	levelTo(desired)\n	showBattleCard(enemy)")



#Player Class

class player():
    def __init__(self):
        self.name = box.nameFormatter(box.nameMaker((out.feed("What is your name? ")),10))

        self.inv = []
        self.monster1 = monster(1,0)
        self.monster2 = monster(1,0)
        self.monster3 = monster(1,0)
    def showCard(self):
        out.output ("\n\n\n\n\n")
        out.output ("- - = . ~ .-=-=#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#=-=-. ~ . = - -")
        out.output ("			" + self.name + "\'s Stats")
        out.output ("")
        self.monster1.showDetails()
        out.output ("")
        self.monster2.showDetails()
        out.output ("")
        self.monster3.showDetails()
        out.output ("\n- - = . ~ .-=-=#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#@#=-=-. ~ . = - -")
    def help(self):
        out.output("Vars:\n	name\n	inv\n	monster1\n	monster2\n	monster3\n\nFunctions:\n	showCard()")

def console():
    consolecont = 1
    while consolecont == 1:
        request = out.feed("Command me. ")
        #general executioner
        if ("exec" in request):
            execCode = request[5:len(request)]
            eval(execCode)

        #battle initialization
        elif ("battle init" in request):
            #battle init | your monster | enemy monster{specieID,level}
            request = request.split()
            #make the arguents that entertain the generated monster.
            request[3] = request[3].split(",")
            request[3] = list(request[3])
            #make an enemy monster using given arguments
            enemy = monster(0, int(request[3][0]))
            enemy.levelTo(int(request[3][1]))
            enemy.showDetails()
            #attempt a battle()
            #out.output (str(request[2]))
            execCode = ("battle(" + str(request[2]) + ", enemy , 0)")
            #out.output(execCode)
            exec(execCode)
            #battle(p1.monster1, enemy, 0)

        elif (("quit" in request) or ("exit" in request) or ("stop" in request)):
            consolecont = 0
        else:
            out.output ("Try again.")
        #leveling up didn't work so now we have the beautiful and versatile exec.
        """elif ("level to" in request):
            request = request.split()
            del request[0]
            del request[0]
            p1.monster1.showDetails()
            cmder = ("pl." + request[0] + ".levelTo(" + request[1] + ")")
            out.output (cmder)
            eval(cmder)
            p1.monster1.showDetails()"""


def attack(m1, move, m2):
    #example: attack(p1.monster1, 1-n, enemy1)

    #raw damage stat from moves list
    #My comments down there bugtest that everything was done globally. It works!! Thanks Python for being so lovely and intuitive!
    rawdmg = m1.learnedMoves[(move-1)][1]
    #out.output ("rawdmg: " + str(rawdmg))
    moddedDmg = math.floor( (rawdmg * m1.attack) * m2.defense)
    #out.output ("moddedDmg: " + str(moddedDmg))
    m2.health -= moddedDmg
    #m2.showBattleCard(1)
    out.output (m1.nickname + " used " + m1.learnedMoves[move-1][0] + " for " + str(moddedDmg) + " damage!" )
    if (m2.health < 0):
        m2.health = 0
    #enemy.showBattleCard(1)

def xpAdder(m1, m2):
        if m1.level < m2.level:
            m1.xp += math.floor(m2.level * 1.35) * m1.level
        elif m1.level > m2.level:
            m1.xp += math.ceil(m2.level * (0.9 / (m1.level - m2.level) ))
        elif m1.level == m2.level:
            m1.xp += math.ceil(m2.level * 1.25) * m1.level
        else:
            out.output ("xp broken, pls fix daddy!")
def battle(m1,m2,pvp):
    if (pvp == 0):
        box.clearScreen()
        out.output (p1.name + "\'s " + m1.nickname + " is battling enemy " + m2.nickname + "!")
        m1.showBattleCard(0)
        m2.showBattleCard(1)
        box.pause()
        box.clearScreen()
        while ((m1.health >= 1) and (m2.health >= 1)):
            m2.showBattleCard(1)
            m1.showBattleCard(0)
            m1.showMoves()
            if m1.health > 0:
                inp = out.feed("\nWhat will " + m1.nickname + " do?\n")
                again = 1
                while again == 1:
                    try:
                        int(inp)
                    except ValueError:
                        out.output ("\nNumbers only!")
                        again = 1
                        inp = out.feed("Try again:\nWhat will " + m1.nickname + " do?\n")
                    except:
                        out.output ("\nSomething went wrong with what you said!")
                        again = 1
                        inp = out.feed("Try again:\nWhat will " + m1.nickname + " do?\n")
                    else:
                        if (int(inp) > m1.howManyMoves()):
                            again = 1
                            out.output ("\nNumber out of range!")
                            inp = out.feed("Try again:\nWhat will " + m1.nickname + " do?\n")
                        else:
                            again = 0
                            break

                attack(m1, int(inp), m2)
                del inp
                del again
            if m2.health > 0:
                attack(m2, random.randint(1,len(m2.learnedMoves)), m1)

            box.pause()
            box.clearScreen()


        if (m1.health > 0):
            xpAdder(m1, m2)
            m2.showBattleCard(1)
            m1.showBattleCard(0)
            out.output("You win!")

        elif (m2.health > 0):
            xpAdder(m2, m1)
            m2.showBattleCard(1)
            m1.showBattleCard(0)
            out.output ("You lose!")
        else:
            out.output ("You broke the game and should not see this message!")




#out.output (box.stringSolver(5, "Jon") + "{}")
#out.output (box.stringSolver(7, "ashkiabaiibelfd") + "{}")
p1 = player()
enemy = monster(0,0)
#out.output (enemy.nickname)
#p1.showCard()
#p1.monster1.showBattleCard(1)
#p1.monster2.showBattleCard(0)
#p1.monster1.levelTo(8)
#enemy.health -= 150
#p1.monster1.levelTo(6)
#out.output (p1.monster1.learnedMoves)
#battle(p1.monster1, enemy, 0)
#attack(p1.monster1, 2, enemy)
#p1.monster1.showMoves()
#p1.showCard()
console()
#import os
#os.system("python Editor.py")
