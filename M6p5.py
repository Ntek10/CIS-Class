#M6p5.py      Nick      10/02

#input
lastName= input("Enter last name: ")

salary= float(input("Enter salary: "))

jobLevel= int(input("Enter your job level: "))

#process

if jobLevel>=10:
    bonusRate=.25

else:
    if jobLevel>=5:
        bonusRate=.20
    else:
        bonusRate=.10

bonusPay= salary*bonusRate

#output

print("-------Summary-------")

print("Last name: ", lastName)

print("Bonus: ",bonusPay)
