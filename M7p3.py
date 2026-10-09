#M7p3.py       Nick      10/08

count= 0

response= input("Would you like to do this program? (YES/NO):")

while response.lower() in ["yes", "y"]:
    lastName= input("Enter your last name: ")
    score1= float(input("Enter exam score 1: "))
    score2= float(input("Enter exam score 2: "))

    average= (score1+score2)/2

    print(f"Studnet: {lastName}  |  Average score: {average:.2f}")

    count+=1

    response= input("Do you want to process another one?: (Yes/No)")

print(f"\nTotal number of students processed:{count}")
