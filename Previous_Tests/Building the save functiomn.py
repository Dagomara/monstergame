monsters = [['null', [['null', 1, 1]]], ['Ladybug', [['Tackle', 6, 0], ['Fly', 10, 3], ['Kiss', 4, 5]]], ['Paperclip', [['Strangle', 6, 0], ['Pinch', 12, 7]]], ['Devile', [['Tackle', 6, 0]]]]
def save(file):
    f = open(file, "w")
    #print("txt opened")
    for monster in monsters:
        f.write("$" + monster[0] + "\n")
        for move in monster[1]:
            f.write("@" + move[0] + ";" + str(move[1]) + ";" + str(move[2]) + "\n")
    f.write("&")
    f.close()

