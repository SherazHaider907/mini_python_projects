unit = input("Is this temperature in (C)elsius or (F)ahrenheit? ").upper()
temp = float(input("Enter the temperature: "))

if unit == "C":
    converted = (temp * 9/5) + 32
    print(f"Temperature in Fahrenheit: {round(converted, 2)}")
elif unit == "F":
    converted = (temp - 32) * 5/9
    print(f"Temperature in Celsius: {round(converted, 2)}")
else:
    print("Invalid unit")