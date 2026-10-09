#M7p4.py     Nick       10/08

totalGrossPay= 0.0

employeeCount= 0

response=input("Do you want to do this program? (Yes/No): ")

while response.lower() in ["yes","y"]:
    lastName= input("Enter last name: ")
    hours= float(input("Enter hours worked: "))
    hourlyRate=float(input("Enter hourly rate: "))

    if hours>40:
        overtimeHours = hours-40
        grossPay= (40 * hourlyRate)+(overtimeHours*hourlyRate*1.5)
    else:
        grossPay= hours*hourlyRate

    print(f"Employee: {lastName} | Gross Pay: ${grossPay:.2f}")

    totalGrossPay += grossPay
    employeeCount+=1

    response=input("Do you want to process another employee: (Yes/No)")

print("\n--- Summary ---")
print(f"Total Gross Pay: ${totalGrossPay:.2f}")
print(f"Total Employees: {employeeCount}")

if employeeCount>0:
    averagePay= totalGrossPay/employeeCount
    print(f"Average Gross Pay: ${averagePay:.2f}")
else:
    print("No employee data entered.")
