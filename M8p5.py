#M8p5.py   Nick     10/21

totalTuitionOwed = 0.0
studentCount = 0

with open("students.txt", "r") as file:
    lines = file.readlines()

print(f"{'Last Name':<12} {'Credits':<10} {'Tuition Owed':<12}")
print("-" * 36)

#loop + process
for i in range(0, len(lines), 3):
    studentName = lines[i].strip()
    districtCode = lines[i+1].strip().upper()
    creditsTaken = int(lines[i+2].strip())
    
    if districtCode == 'I':
        costPerCredit = 250.00
    else:
        costPerCredit = 500.00
        
    tuitionOwed = creditsTaken * costPerCredit
    totalTuitionOwed += tuitionOwed
    studentCount += 1
    
    print(f"{studentName:<12} {creditsTaken:<10} ${tuitionOwed:<11,.2f}")

#output
print("-" * 36)
print(f"Sum of all tuition owed: ${totalTuitionOwed:,.2f}")
print(f"Total number of students: {studentCount}")
