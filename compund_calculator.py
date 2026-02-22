# python compund interest calculator

principal = 0
rate = 0
time = 0

while principal <= 0:
    principal = float(input("Enter the principal amount: "))
    if principal <= 0:
        print("Principal amount must be greater than 0. Please try again.")


while rate <= 0:
    rate = float(input("Enter the rate of interest: "))
    if rate <= 0:
        print("Rate of interest must be greater than 0. Please try again.")

while time <= 0:
    time = float(input("Enter the time period in Years: "))
    if time <= 0:
        print("Time period must be greater than 0. Please try again.")


totle = principal * (1 + rate / 100) ** time
print(f"The total amount after {time} years is: ${totle:.2f}")