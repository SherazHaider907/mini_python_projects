import random

options = ["rock", "paper", "scissors"]

player_score = 0
computer_score = 0

is_running = True

while is_running:

    player_choice = input("\nEnter your choice (rock, paper, scissors) or 'q' to quit: ").lower()

    if player_choice == "q":
        print("\nGame Over!")
        print(f"Final Score -> You: {player_score} | Computer: {computer_score}")
        break

    if player_choice not in options:
        print("Invalid choice! Try again.")
        continue

    computer_choice = random.choice(options)

    print(f"\nPlayer: {player_choice}")
    print(f"Computer: {computer_choice}")

    if player_choice == computer_choice:
        print("It's a tie!")

    elif (
        (player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "paper" and computer_choice == "rock") or
        (player_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win!")
        player_score += 1

    else:
        print("Computer wins!")
        computer_score += 1

    print(f"Score -> You: {player_score} | Computer: {computer_score}")