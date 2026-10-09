#M7p5.py       Nick      10/08

total_discounts = 0.0

response = input("Do you want to run this program? (Yes/No): ")

while response.lower() in ["yes", "y"]:
    quantity = int(input("Enter item quantity: "))
    price = float(input("Enter unit price: "))
    
    extended_price = quantity * price
    
    if extended_price > 10000.00:
        discount_rate = 0.25
    else:
        discount_rate = 0.10
        
    discount_amount = extended_price * discount_rate
    total_amount = extended_price - discount_amount
    
    print(f"Extended Price: ${extended_price:.2f}")
    print(f"Discount Amount ({int(discount_rate * 100)}%): ${discount_amount:.2f}")
    print(f"Total Amount: ${total_amount:.2f}")
    
    total_discounts += discount_amount
    
    response = input("Do you want to process another order? (Yes/No): ")

print(f"\nTotal Discount Amount across all orders: ${total_discounts:.2f}")

