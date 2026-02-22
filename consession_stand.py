menu = {
    "hot dog": 2.50,
    "hamburger": 3.00,
    "fries": 1.50,
    "soda": 1.00,
    "pizza": 4.00,
    "ice cream": 2.00,
    "popcorn": 1.75,
    "candy": 1.25
}

cart = []
total = 0
print("---------MENU---------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("----------------------")

while True:
    food = input("Enter the food item you want to order (or 'q' to finish): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
        
print("-----YOUR ORDER-----")
for food in cart:
    total += menu.get(food)
    print(food , end = " ")

print()
print(f"Total: ${total:.2f}")
