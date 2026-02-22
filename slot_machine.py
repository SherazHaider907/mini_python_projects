# python Slot Machine 
import random
def spin_row():
    symbols = ["🍒", "🍋", "🍊", "🔔", "🍉", "⭐", "🍇"]

    # result = []
    # for symbol in range(3):
    #     result.append(random.choice(symbols))
    # return result

    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print(" | ".join(row))

def get_payout(row,bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 3
        elif row[0] == "🍋":
            return bet * 4
        elif row[0] == "🍊":
            return bet * 5
        elif row[0] == "🔔":
            return bet * 10
        elif row[0] == "🍉":
            return bet * 7
        elif row[0] == "⭐":
            return bet * 20
        elif row[0] == "🍇":
            return bet * 9
    return 0


def main():
    while True:
        starting_balance = input("Enter the amount of money you want to start with: ")

        if not starting_balance.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        balance = int(starting_balance)

        if balance <= 0:
            print("Amount must be greater than 0.")
            continue

        break

    print("***********************")
    print("Welcome to python Slots")
    print("Symbols: 🍒, 🍋, 🍊, 🔔,🍉, ⭐,🍇")
    print("***********************")

    while balance > 0:
        print(f"Your balance is: ${balance}")

        bet = input("Enter your bet amount: ")

        if not bet.isdigit():
            print("Invalid input. Please enter a number.")
            continue
        bet = int(bet)
        if bet > balance:
            print("Insufficient funds")
            continue

        if bet <= 0:
            print("Bet must be greater than 0")
            continue

        balance -= bet

        row =  spin_row()
        print("Spinning...\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"Congratulations! You won ${payout}")
        else:
            print("Sorry you lost this round")

        balance += payout

        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != "y":
            break

    print(f"Game over! Your final balance is: ${balance}")
if __name__ == "__main__":
    main()