#M11.p4       Nick       11/19

def calculateBowlingAverage(game1, game2, game3, handicap):
    averageScore = (game1 + game2 + game3) / 3
    averageWithHandicap = averageScore + handicap
    return averageScore, averageWithHandicap


def main():
    lastName = input("Enter bowler's last name: ")
    game1 = float(input("Enter game 1 score: "))
    game2 = float(input("Enter game 2 score: "))
    game3 = float(input("Enter game 3 score: "))
    handicap = float(input("Enter handicap: "))

    averageScore, averageWithHandicap = calculateBowlingAverage(game1, game2, game3, handicap)

    print(f"Bowler Last Name: {lastName}")
    print(f"Average Score: {averageScore:.2f}")
    print(f"Average Score with Handicap: {averageWithHandicap:.2f}")


main()
