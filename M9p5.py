#M9p5.py   Nick     11/01

def computeTuition(creditHours, districtCode):
    code = districtCode.upper()
    if code == 'I':
        return creditHours * 250.0
    else:
        return creditHours * 550.0

totalTuitionOwed = 0.0

while True:
    studentName = input("Enter student last name (or 'q' to quit): ")
    if studentName.lower() == 'q':
        break
    creditHours = float(input("Enter credit hours: "))
    districtCode = input("Enter district code (I or O): ")
    
    tuition = computeTuition(creditHours, districtCode)
    totalTuitionOwed += tuition
    
    print(f"Student: {studentName} | Tuition Owed: ${tuition:.2f}\n")

print(f"\nTotal tuition owed for all students: ${totalTuitionOwed:.2f}")
