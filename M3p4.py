make=input("Make: ")

model=input("Model: ")

msrp=float(input("MSRP: $"))

discountPercent=float(input("Discount Percent: "))


amountOff= msrp * discountPercent

discountedPrice= msrp - amountOff


print("------------------------------------")

print("Make: ", make)

print("Model: ", model)

print("Msrp: $", msrp)

print("Discount Percent: ", discountPercent)

print("Amount off: $", amountOff)

print("Discounted price: $", discountedPrice)
