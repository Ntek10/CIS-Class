#M10p1.py   Nick     11/08

def computeForecast(month, sales):
    m = month.capitalize()
    if m in ['Jan', 'Feb', 'Mar']:
        pct = 0.10
    elif m in ['Apr', 'May', 'Jun']:
        pct = 0.15
    elif m in ['Jul', 'Aug', 'Sep']:
        pct = 0.20
    else:
        pct = 0.25
    return sales * (1 + pct)

while True:
    userChoice = input("Do you want to run the program? (Yes or No): ").strip().lower()
    if userChoice != 'yes':
        break
        
    lastName = input("Enter last name: ")
    monthInput = input("Enter month (e.g., Jan, Feb): ")
    salesAmount = float(input("Enter sales amount: "))
    
    forecastedSales = computeForecast(monthInput, salesAmount)
    print(f"Salesperson: {lastName} | Month: {monthInput} | Next Month's Forecasted Sales: ${forecastedSales:.2f}\n")
