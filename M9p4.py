#M9p4.py   Nick   11/01

def getPayRate(jobCode):
    code = jobCode.upper()
    if code == 'L':
        return 25.0
    elif code == 'A':
        return 30.0
    elif code == 'J':
        return 50.0
    return 0.0

totalGrossPay = 0.0

while True:
    lastName = input("Enter employee last name (or 'q' to quit): ")
    if lastName.lower() == 'q':
        break
    jobCode = input("Enter job code (L, A, J): ")
    hoursWorked = float(input("Enter hours worked: "))
    
    rate = getPayRate(jobCode)
    
    if hoursWorked > 40:
        grossPay = (40 * rate) + ((hoursWorked - 40) * (rate * 1.5))
    else:
        grossPay = hoursWorked * rate
        
    totalGrossPay += grossPay
    print(f"Employee: {lastName} | Gross Pay: ${grossPay:.2f}\n")

print(f"\nTotal of all gross pay: ${totalGrossPay:.2f}")
