import random

lowest_number = 1
highest_number = 100
answer = random.randint(lowest_number, highest_number)
guesses = 0
is_running = True

print("Welcome to the number guessing game!")
print(f"Select a number between {lowest_number} and {highest_number}.")

while is_running:

    guess = input("Your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < answer:
            print("Too low! Try again.")
        elif guess > answer:
            print("Too high! Try again.")
        else:
            print(f"🎉 Congratulations! You've guessed the number {answer} in {guesses} guesses!")
            is_running = False
    else:
        print("Please enter a valid number.")