#M5p4.py    Nick    09/23

#input
appliance= str(input("Name of appliance: "))
                
#input
applianceCost= float(input("Cost of appliance: "))

#process
if applianceCost> 1000:
    warranty= applianceCost * .10
else:
    warranty= applianceCost * .05

#process
totalPrice= applianceCost+warranty

#output
print("Name of appliance: ",appliance)

#output
print("Cost of appliance: ", applianceCost)

#output
print("Warranty cost: ", warranty)

#output
print("Total cost: ", totalPrice)

