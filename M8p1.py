#M8p1.py      Nick      10/18


#input
principalAmount= float(input("Enter principal amount: "))
interestRate= float(input("Enter interest rate as a decimal: "))

#process
totalInterest =0.0

#creating the table
print("\nFormatted Output\n")
print(f"{'Year':<6} {'Beginning':<12} {'Ending':<12}")
print(f"{'':<6} {'Balance':<12} {'Balance':<12}")

#The loop for the 5 years.
for year in range(1,6):
    beginningBalance=principalAmount
    interest= beginningBalance*interestRate
    endingBalance= beginningBalance + interest

    #the total interest tracker
    totalInterest += interest

    beginning=f"${beginningBalance:,.2f}"
    ending=f"${endingBalance:,.2f}"


    print(f"{year:<6} {beginning:<12} {ending:<12}")

    principalAmount = endingBalance

print(f"\nTotal interest earned: ${totalInterest:,.2f}")
