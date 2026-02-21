weight = float(input("Enter your weight: "))
unit = input("Enter unit (K for kg, L for lbs): ").upper()

if unit == "K":
    print("Weight in pounds:", round(weight * 2.2, 2))
elif unit == "L":
    print("Weight in kg:", round(weight / 2.2, 2))
else:
    print("Invalid unit")