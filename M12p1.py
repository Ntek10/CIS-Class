#M12P1    Nick   11/21

def displayNames(lastNames):
    i = 0
    while i < len(lastNames):
        print(lastNames[i])
        i = i + 1


def displayNamesReverse(lastNames):
    i = len(lastNames) - 1
    while i >= 0:
        print(lastNames[i])
        i = i - 1


def main():
    lastNames = [
        "Smith", "Johnson", "Brown", "Taylor", "Anderson",
        "Thomas", "Jackson", "White", "Harris", "Martin"
    ]

    print("Last Names:")
    displayNames(lastNames)

    print("\nLast Names in Reverse:")
    displayNamesReverse(lastNames)


main()
