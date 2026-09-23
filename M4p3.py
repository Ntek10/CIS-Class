mealPrice = float(input("Enter total for the meal: "))

tip15= mealPrice * .15
total15= mealPrice + tip15

tip18= mealPrice * .18
total18= mealPrice + tip18

tip20= mealPrice * .20
total20= mealPrice + tip20

print("With the 15% tip: ")
print()
print(f"Total: {mealPrice:.2f}")
print(f"Tip: {tip15:.2f}")
print(f"Total with tip: {total15:.2f}")

print("---------------------------------------")

print("With the 18% tip: ")
print()
print(f"Total: {mealPrice:.2f}")
print(f"Tip: {tip18:.2f}")
print(f"Total with tip: {total18:.2f}")

print("---------------------------------------")

print("With the 20% tip: ")
print()
print(f"Total: {mealPrice:.2f}")
print(f"Tip: {tip20:.2f}")
print(f"Total with tip: {total20:.2f}")

