ticker= input("Type your stock symbol: ")

shares= int(input("Type your amount of shares: "))

cost= float(input("Type your cost per share: "))


invested= shares * cost

print("Stock:", ticker)
print("Amount invested: $", invested)


