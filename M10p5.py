#M10p5.py   Nick     11/09

def computeAssessedValue(county, marketValue):
    c = county.capitalize()
    if c == 'Cook':
        pct = 0.90
    elif c == 'Dupage':
        pct = 0.80
    elif c == 'Mchenry':
        pct = 0.75
    elif c == 'Kane':
        pct = 0.60
    else:
        pct = 0.70
    return marketValue * pct

totalMarketValueSum = 0.0
totalAssessedValueSum = 0.0

while True:
    userChoice = input("Do you want to run the program? (Yes or No): ").strip().lower()
    if userChoice != 'yes':
        break
        
    countyName = input("Enter county: ")
    marketValueInput = float(input("Enter market value of home: "))
    
    assessedValue = computeAssessedValue(countyName, marketValueInput)
    
    totalMarketValueSum += marketValueInput
    totalAssessedValueSum += assessedValue
    
    print(f"County: {countyName} | Market Value: ${marketValueInput:.2f} | Assessed Value: ${assessedValue:.2f}\n")

print(f"\nTotal of all market values: ${totalMarketValueSum:.2f}")
print(f"Total of all assessed values: ${totalAssessedValueSum:.2f}")
