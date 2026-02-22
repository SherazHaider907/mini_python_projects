import random

dice_art = {
    1: (
        "┌─────┐\n"
        "│     │\n"
        "│  ●  │\n"
        "│     │\n"
        "└─────┘"
    ),
    2: (
        "┌─────┐\n"
        "│ ●   │\n"
        "│     │\n"
        "│   ● │\n"
        "└─────┘"
    ),
    3: (
        "┌─────┐\n"
        "│ ●   │\n"
        "│  ●  │\n"
        "│   ● │\n"
        "└─────┘"
    ),
    4: (
        "┌─────┐\n"
        "│ ●   ● │\n"
        "│       │\n"
        "│ ●   ● │\n"
        "└─────┘"
    ),
    5: (
        "┌─────┐\n"
        "│ ●   ● │\n"
        "│   ●   │\n"
        "│ ●   ● │\n"
        "└─────┘"
    ),
    6: (
        "┌─────┐\n"
        "│ ●   ● │\n"
        "│ ●   ● │\n"
        "│ ●   ● │\n"
        "└─────┘"
    )
}

dice = []
total = 0  
num_of_dice = int(input("How many dice do you want to roll? "))

for die in range(num_of_dice):
    dice.append(random.randint(1, 6))

# print dice art
for die in range(num_of_dice):
    for line in dice_art[dice[die]].splitlines():
        print(line)

# calculate total
for die in dice:
    total += die  

print(f"total: {total}")  