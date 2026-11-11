#M9p3.py     nick     11/01/2026

def computeMpg(miles, gallons):
    if gallons == 0:
        return 0.0
    return miles / gallons

tripCount = 0

while True:
    destinationCity = input("Enter destination city (or 'q' to quit): ")
    if destinationCity.lower() == 'q':
        break
    milesTravelled = float(input("Enter miles travelled: "))
    gallonsUsed = float(input("Enter gallons used: "))
    
    mpg = computeMpg(milesTravelled, gallonsUsed)
    tripCount += 1
    
    print(f"Destination: {destinationCity} | Miles: {milesTravelled} | MPG: {mpg:.2f}\n")

print(f"\nTotal number of trips entered: {tripCount}")
