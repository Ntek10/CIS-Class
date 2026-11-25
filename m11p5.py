#m11p5.py   Nick        11/25

total = 0.0
tax = 0.0


def calculateTotalAndTax(quantity, unitPrice):
    global total, tax
    total = quantity * unitPrice
    tax = total * 0.07


def main():
    quantity = int(input("Enter quantity: "))
    unitPrice = float(input("Enter unit price: "))

    calculateTotalAndTax(quantity, unitPrice)

    print(f"Total: ${total:.2f}")
    print(f"Tax (7%): ${tax:.2f}")


main()
