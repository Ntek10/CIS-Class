#M6P1      #Nick     #10/01

#input
quantity= int(input("Quantity of widgets; "))

if quantity>10000:
    price = 10.00

else:
    if quantity>=5000:
        price = 20.00

    else:
        price=30.00


extendedPrice= quantity*price
taxAmount= extendedPrice*.07
totalPrice= extendedPrice+taxAmount

print(f"Extended Price: ${extendedPrice:>10.2f}")
print(f"Tax Amount: ${taxAmount:>10.2f}")
print(f"Total Price: ${totalPrice:>10.2f}")
