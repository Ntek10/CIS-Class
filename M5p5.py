#M5p5.py    Nick     09/23

#input
lastName= str(input("Enter last name: "))

#input
dependents= int(input("Number of dependants: "))

#input
grossIncome= float(input("Gross income: "))


#process
adjGrossIncome= grossIncome-dependents * 12000

#process
if adjGrossIncome > 50000:
    taxRate= .20
else:
    taxRate=.10

#process
incomeTax= adjGrossIncome * taxRate

#process
if incomeTax<0:
    incomeTax=100

#output
print("Last name: ", lastName)

#output
print("Gross income: ",grossIncome)

#output
print("Number of dependents: ", dependents)

#output
print("Adjusted gross income: ", adjGrossIncome)

#output
print("Income tax: ", incomeTax)
