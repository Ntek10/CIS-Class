#M8p3.py     Nick  10/21

totalBonus = 0.0

#this is to read and open the file
with open ("List of Names.py", "r") as file:
    lines= file.readlines()

print(f"{'Last Name':<12} {'Salary':<12} {'Bonus':<12}")
print("-"*38)

#Loop
for i in range(0, len(lines), 2):
    name=lines[i].strip()
    salary= float(lines[i+1].strip())

    #bonus rate
    if salary>= 100000.0:
        bonusRate=.20
    elif salary== 50000.0:
        bonusRate=.15
    else:
        bonusRate=.10

    bonus = salary * bonusRate
    totalBonus += bonus

    print(f"{name:<12} ${salary:<11,.2f} ${bonus:<11,.2f}")

#output

print("-"*38)
print(f"Total bonuses paid out: ${totalBonus:,.2f}")

        
