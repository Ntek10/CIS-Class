#M8p4.py   nick    10/21


totalExtendedPrice = 0.0
orderCount = 0

with open("orders.txt", "r") as file:
    lines = file.readlines()

print(f"{'Item':<10} {'Qty':<6} {'Price':<10} {'Ext Price':<10}")
print("-" * 40)


#loop
for i in range(0, len(lines), 3):
    itemName = lines[i].strip()
    quantity = int(lines[i+1].strip())
    unitPrice = float(lines[i+2].strip())
    
    extendedPrice = quantity * unitPrice
    totalExtendedPrice += extendedPrice
    orderCount += 1
    
    print(f"{itemName:<10} {quantity:<6} ${unitPrice:<9.2f} ${extendedPrice:<9.2f}")

averageOrder = totalExtendedPrice / orderCount if orderCount > 0 else 0.0

#output
print("-" * 40)
print(f"Sum of all extended prices: ${totalExtendedPrice:,.2f}")
print(f"Number of orders: {orderCount}")
print(f"Average order: ${averageOrder:,.2f}")
