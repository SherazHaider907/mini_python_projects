operator = input("Enter the operator you want to use (+, -, *, /):")
num1 = float(input("Enter the First Number:"))
num2 = float(input("Enter the Seconf Number:"))

if operator == "+":
    result = num1 + num2
    print(round(result,3))
elif operator == "-":
    result = num1 - num2
    print(round(result,3))
elif operator == "*":
    result = num1 * num2
    print(round(result,3))
elif operator == "/":
    result = num1 / num2
    print(round(result,3))
else:
    print(f"Invalid operator: {operator}. Please use one of the following: +, -, *, /.")