purchasedPrice= int(input("Purchase price per share: "))

currentPrice= float(input("Current stock price: "))

quantityStock= int(input("Quantity of stock: "))

stockValue= (currentPrice - purchasedPrice) * quantityStock

print("Value of stock(s): ", stockValue)
