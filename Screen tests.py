def screen1():
    print ("Screen 1")
def screen2():
    print ("Screen 2")
def screen3():
    print ("Screen 3")
screen = 1
while 1 == 1:
    if screen == 1:
        screen1()
        if int(input("forward?" )) == 1:
            print ("To screen 2")
            screen = 2
    if screen == 2:
        screen2()
        if int(input("forward?" )) == 1:
            print ("To screen 3")
            screen = 3
        if int(input("back?" )) == 1:
            print ("To screen 1")
            screen = 1
    if screen == 3:
        screen3()
        if int(input("back?" )) == 1:
            print ("To screen 2")
            screen = 2


#Box of useful stuff

def nameFormatter(string):
    string = string.strip()
    string = string.title()
    return string


def clearScreen():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


def pause():
    input("Press ENTER to continue.")


def stringSolver(chars, string):
    #takes a string and makes it chars characters long, and filling the rest with whitespace if necessary.
    if len(string) > chars:
        string = string[0:chars]
    else:
        spaces = (chars - len(string))
        for i in range(spaces):
             string +=(" ")
    return string
