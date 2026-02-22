# python Banking System

# 1.Show Balance
# 2.Deposit
# 3.Withdraw

def show_balance(balance):
    print(f"Your current balance is: ${balance:.2f}")

def deposit():
    amount = float(input("Enter the amount to deposit: "))
    if amount < 0:
        print("That not a valid amount")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter the amount to withdraw: "))
    if amount > balance:
        print("Insufficient funds")
        return 0
    elif amount < 0:
        print("That not a valid amount")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("Banking System")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choise = input("Choose an option(1-4): ")

        if choise == "1":
            show_balance(balance)
        elif choise == "2":
            balance += deposit()
        elif choise == "3":
            balance -= withdraw(balance)
        elif choise == "4":
            is_running = False
        else:
            print("Invalid option. Please choose a number between 1 and 4.")


    print("Thank you ! Have a nice day ")

if __name__ == "__main__":
    main()