#M10p3.py    Nick    11/09

def computeOutTheDoor(msrp, make, model, evCode):
    vehicleName = f"{make} {model}".strip()
    
    if evCode.upper() == 'Y':
        discountPct = 0.30
    elif vehicleName == 'Honda Accord':
        discountPct = 0.10
    elif vehicleName == 'Toyota Rav4':
        discountPct = 0.15
    else:
        discountPct = 0.05
        
    newMsrp = msrp * (1 - discountPct)
    totalPrice = newMsrp * 1.07
    return totalPrice, newMsrp

totalMsrpSum = 0.0
totalSalesPriceSum = 0.0

while True:
    userChoice = input("Do you want to run the program? (Yes or No): ").strip().lower()
    if userChoice != 'yes':
        break
        
    carMake = input("Enter make: ")
    carModel = input("Enter model: ")
    evCodeInput = input("Is it an electric vehicle? (Y or N): ")
    carMsrp = float(input("Enter MSRP (sticker price): "))
    
    finalPrice, discountedMsrp = computeOutTheDoor(carMsrp, carMake, carModel, evCodeInput)
    
    totalMsrpSum += carMsrp
    totalSalesPriceSum += finalPrice
    
    print(f"Car: {carMake} {carModel} | Out-the-Door Price: ${finalPrice:.2f}\n")

print(f"\nSum of all MSRPs: ${totalMsrpSum:.2f}")
print(f"Sum of all final sales prices: ${totalSalesPriceSum:.2f}")
