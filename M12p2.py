#M12p2.py    Nick   11/21

def displayStudents(lastNames, examScores):
    i = 0
    while i < len(lastNames):
        print(lastNames[i], "-", examScores[i])
        i = i + 1


def displayStudentsReverse(lastNames, examScores):
    i = len(lastNames) - 1
    while i >= 0:
        print(lastNames[i], "-", examScores[i])
        i = i - 1


def main():
    lastNames = [
        "Smith", "Johnson", "Brown", "Taylor", "Anderson",
        "Thomas", "Jackson", "White", "Harris", "Martin"
    ]
    examScores = [88, 92, 76, 85, 95, 79, 91, 84, 89, 93]

    print("Names and Scores:")
    displayStudents(lastNames, examScores)

    print("\nNames and Scores in Reverse:")
    displayStudentsReverse(lastNames, examScores)


main()
