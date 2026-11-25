#M11.p1     Nick     11/19

def calculateDiscount(quantity, price, discountRate):
    
    discountDecimal = discountRate / 100
    subtotal = quantity * price
    discountAmount = subtotal * discountDecimal
    discountedPrice = subtotal - discountAmount
    return discountAmount, discountedPrice


def main():
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))
    discountRate = float(input("Enter discount rate (e.g., 20 for 20%): "))

    discountAmount, discountedPrice = calculateDiscount(quantity, price, discountRate)

    print(f"Quantity: {quantity}")
    print(f"Price: ${price:.2f}")
    print(f"Discount Amount: ${discountAmount:.2f}")
    print(f"Discounted Price: ${discountedPrice:.2f}")


main()
