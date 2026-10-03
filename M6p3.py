#M6p3.py      Nick     10/02

#input
principleAmnt= float(input(" Enter principle amount: "))

yearMaturity= int(input("Years to maturity: "))

#process

if principleAmnt>100000 and yearMaturity==5:
    interestRate= .06

else:
    if principleAmnt>=50000 and yearMaturity==10:
        interestRate= .05

    else:
        if principleAmnt>=50000 and yearMaturity==5:
            interestRate=.04
        else:
            interestRate=.02

firstYear= (principleAmnt*interestRate)

#output

print("------- Summary -------")

print("Principle: ", principleAmnt)

print("Interest rate: ", interestRate)

print("Interest amount: ",firstYear)
