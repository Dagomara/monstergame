#levelOfDetail:
#1: basic command line.
#2: GUI available/adaptable. HTML/CSS, TKinter, etc.
#3: GUI available with graphics, meaning sprites.
#4: GUI available with advanced graphics, meaning 3D models.
levelOfDetail = 1

"""

Command Line outputs!
What the game was built on originally.

"""
if levelOfDetail == 1:
    def feed(question):
        return (input(question))
    def output(stuff):
        print(stuff)
    def clearScreen():
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

elif levelOfDetail == 2:
    platform = "tkinter"
    if platform == "tkinter":
        pass
    elif platform == "web":
        pass
    else:
        pass
