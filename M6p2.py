#M6p2.py        Nick       10/02

#input
partNumber= input("Enter a part number: ")

quantity= int(input("Enter the quantity: "))

#process
if partNumber== "10" or partNumber== "55":
    unitCost= 1.00
else:
    if partNumber== "99":
        unitCost= 2.00

    else:
        if partNumber=="80" or partNumber=="70":
            unitCost=3.00

        else:
            unitCost=5.00

totalCost= (quantity*unitCost)

#output
print("Part number: ",partNumber)

print("Cost per unit: ",unitCost)

print("Total cost: ",totalCost)
