#M9p1.py            Nick          11/01/2026

def computeExtendedPrice(qty, price):
    total = qty * price
    if total > 10000.00:
        total = total * 0.90
    return total

totalExtPrice = 0.0

while True:
    qtyInput = input("Enter quantity (or 'q' to quit): ")
    if qtyInput.lower() == 'q':
        break
    priceInput = input("Enter unit price: ")
    
    qty = float(qtyInput)
    price = float(priceInput)
    
    extPrice = computeExtendedPrice(qty, price)
    totalExtPrice += extPrice
    
    print(f"Qty: {qty} | Price: ${price:.2f} | Extended Price: ${extPrice:.2f}\n")

print(f"\nTotal Extended Price: ${totalExtPrice:.2f}")
