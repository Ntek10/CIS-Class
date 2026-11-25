#M12p5.py   Nick    11/22



def loadPlayers(fileName):
    playerNames = []
    battingAverages = []

    myFile = open(fileName, "r")
    for line in myFile:
        line = line.strip()
        if line != "":
            parts = line.split(",")
            playerNames.append(parts[0].strip())
            battingAverages.append(float(parts[1].strip()))
    myFile.close()

    return playerNames, battingAverages


def displayPlayers(playerNames, battingAverages):
    i = 0
    while i < len(playerNames):
        print(playerNames[i], "-", battingAverages[i])
        i = i + 1


def searchPlayer(playerNames, battingAverages, targetName):
    found = False
    i = 0

    while i < len(playerNames):
        if playerNames[i].lower() == targetName.lower():
            print("Found:", playerNames[i], "-", battingAverages[i])
            found = True
        i = i + 1

    if found == False:
        print("Name not found")


def main():
    playerNames, battingAverages = loadPlayers("players.txt")

    print("All Players:")
    displayPlayers(playerNames, battingAverages)

    choice = input("\nEnter a last name to search (or 'exit' to quit): ")
    while choice.lower() != "exit":
        searchPlayer(playerNames, battingAverages, choice)
        choice = input("\nEnter a last name to search (or 'exit' to quit): ")


main()
