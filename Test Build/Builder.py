import os

def buildMe():
    
    path = os.getcwd()
    print("The current working directory is " + path + ". I hope this is correct!")
    input("I paused installation so you can exit if you need to.")
    
    """

    Box of useful stuff

    """
    f = open("usefulBox.py","w+")
    f.write(usefulBoxCode)
    f.close()

    """

    Saves and defaultMons

    """
    players = input("how many players?")
    try:
        path = "Saves"
        os.mkdir(path)
        #print("saves worked")
        os.chdir(path)
    except OSError:
        print("Failed to make the %s path." % path)
    else:
        print("/Saves path created and loaded.")
    for i in range(int(players)):
        player = "p" + str(i + 1)
        try:
            os.mkdir(player)
            os.chdir(player)
        except OSError:
            print("Failed to make the /" + player + " path.")
        else:
            print("/" + player + " path created and loaded.")
        f = open((player + ".inf.txt"), "w+")
        f.close()
        f = open((player + ".mon.txt"), "w+")
        f.write(defaultMonsTxt)
        f.close()
        os.chdir("../")
        print(player + " done.")
    os.chdir("../")
    f = open(("game.py"), "w+")
    f.write(gameCode)
    f.close()
    f = open("Editor.py","w+")
    f.write(editorCode)
    f.close()
    del f
    del player
    del players


gameCode = """"""

editorCode = """"""

defaultMonsTxt ="""$null
@null;1;1
$Ladybug
@Tackle;6;0
@Fly;10;3
@Kiss;4;5
$Paperclip
@Strangle;6;0
@Pinch;12;7
$Devile
@Tackle;6;0
$Lohgan
@Tackle;6;0
@Swallow;10;4
@Lego Gun;15;6
&
"""    

usefulBoxCode = """
#codegoesherefellas
"""
buildMe()
