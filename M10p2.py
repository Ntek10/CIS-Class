#M10p2.py    Nick     11/08

def computeWallArea(length, width, height):
    return (2 * length * height) + (2 * width * height)

while True:
    userChoice = input("Do you want to run the program? (Yes or No): ").strip().lower()
    if userChoice != 'yes':
        break
        
    roomLength = float(input("Enter room length: "))
    roomWidth = float(input("Enter room width: "))
    roomHeight = float(input("Enter room height: "))
    
    wallSqFt = computeWallArea(roomLength, roomWidth, roomHeight)
    gallonsNeeded = wallSqFt / 50.0
    
    print(f"Wall Square Footage: {wallSqFt:.2f} sq ft")
    print(f"Gallons of paint needed: {gallonsNeeded:.2f}\n")
