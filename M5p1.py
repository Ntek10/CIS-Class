#M5p1.py     Nick     09/23

#input
quantity= int(input("Enter quantity of item: "))
#process
if quantity>= 1000:
    unitPrice=3.00
#process
if quantity< 1000:
    unitPrice=5.00

#process
extendedPrice= quantity*unitPrice

#process
taxPercent= round(.07*extendedPrice, 2)

#Process
totalPrice= extendedPrice+taxPercent

#output
print("Quantity: ",quantity)

#output
print("Unit price: ", unitPrice)

#output
print("Extended price: ", extendedPrice)

#output
print(f"Tax : ", taxPercent)

#output
print("Total: ", totalPrice)


