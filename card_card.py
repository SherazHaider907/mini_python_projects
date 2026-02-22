# python cridit card validation program



sum_odd_digits = 0
sum_even_digits = 0
total = 0

# step 1 remover any '-' 0r " " from the card number

card_number = input("Enter your card number: ")
card_number = card_number.replace("-", "")
card_number = card_number.replace(" ", "")
card_number = card_number[::-1]


# step 2 add all digits in the odd places from right to left
for x in card_number[::2]:
    sum_odd_digits += int(x)

# step 3 Double every second digit from right to left
for x in card_number[1::2]:
    x = int(x) * 2
    if x >= 10:
        sum_even_digits += (1 + (x % 10))
    else:
        sum_even_digits += x

# step 4 add the results from step 2 and step 3
total = sum_odd_digits + sum_even_digits

# step 5 if the total is divisible by 10, the card number is valid
if total % 10 == 0:
    print("The card number is valid.")
else:
    print("The card number is invalid.")
    