#M5p2.py     nick     09/23

#input
itemUnit= str(input("Item: "))
itemQuantity= int(input("Quantity of item: "))

#process
if itemUnit == "A":
    unitprice= 10.00
else:
    unitPrice=20.00

extendedPrice= unitPrice * itemQuantity

#output

print("Item: ",itemUnit)

print("Unit price: ",unitPrice)

print("Extended price", extendedPrice)
