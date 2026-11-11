#M10p4.py    Nick  11/09

def computeTicketPrice(miles):
    if miles >= 30:
        return 12
    elif miles >= 20:
        return 10
    elif miles >= 10:
        return 8
    else:
        return 5

totalTicketPriceSum = 0.0

while True:
    userChoice = input("Do you want to run the program? (Yes or No): ").strip().lower()
    if userChoice != 'yes':
        break
        
    lastName = input("Enter last name: ")
    milesFromChicago = float(input("Enter miles from downtown Chicago: "))
    
    ticketPrice = computeTicketPrice(milesFromChicago)
    totalTicketPriceSum += ticketPrice
    
    print(f"Passenger: {lastName} | Ticket Price: ${ticketPrice:.2f}\n")

print(f"\nTotal sum of all ticket prices: ${totalTicketPriceSum:.2f}")
