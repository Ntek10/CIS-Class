#M11.p2     Nick     11/19

def calculateExamStats(exam1, exam2, exam3):
    totalPoints = exam1 + exam2 + exam3
    averageScore = totalPoints / 3
    return totalPoints, averageScore


def main():
    lastName = input("Enter student's last name: ")
    exam1 = float(input("Enter exam 1 score: "))
    exam2 = float(input("Enter exam 2 score: "))
    exam3 = float(input("Enter exam 3 score: "))

    totalPoints, averageScore = calculateExamStats(exam1, exam2, exam3)

    print(f"Student Last Name: {lastName}")
    print(f"Total Points: {totalPoints:.2f}")
    print(f"Average Exam Score: {averageScore:.2f}")


main()
