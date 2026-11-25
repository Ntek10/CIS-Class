#M12p3.py   Nick  11/22
def loadFileData(fileName):
    lastNames = []
    scores = []

    myFile = open(fileName, "r")
    for line in myFile:
        line = line.strip()
        if line != "":
            parts = line.split(",")
            lastNames.append(parts[0].strip())
            scores.append(float(parts[1].strip()))
    myFile.close()

    return lastNames, scores


def showHighAndLow(lastNames, scores):
    highVar = 0
    highIndex = 0
    lowVar = 999
    lowIndex = 0

    i = 0
    while i < len(scores):
        if scores[i] > highVar:
            highVar = scores[i]
            highIndex = i

        if scores[i] < lowVar:
            lowVar = scores[i]
            lowIndex = i

        i = i + 1

    print("Highest Score:", lastNames[highIndex], "-", highVar)
    print("Lowest Score:", lastNames[lowIndex], "-", lowVar)


def main():
    lastNames, scores = loadFileData("scores.txt")
    showHighAndLow(lastNames, scores)


main()
