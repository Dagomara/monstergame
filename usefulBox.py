"""

Box of useful stuff

"""

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


def nameMaker(string, length):
    if len(string) <= length:
        return string
    else:
        ex = input("That name doesn't work! Try having " + str(length) + " or less characters!\n>>> ")
    while len(ex) > length:
        ex = input("That name doesn't work! Try having " + str(length) + " or less characters!\n>>> ")
    return ex
    del ex

#print ("Your name is " + nameMaker(input("What's your name? "), 7) + ".")
