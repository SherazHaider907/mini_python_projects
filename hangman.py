import random

# Word list
words = ["apple", "banana", "cherry", "date", "elderberry"]

# Hangman ASCII Art
hangman_art = {
    0: ("""
   -----
   |   |
       |
       |
       |
       |
 =========
"""),
    1: ("""
   -----
   |   |
   O   |
       |
       |
       |
 =========
"""),
    2: ("""
   -----
   |   |
   O   |
   |   |
       |
       |
 =========
"""),
    3: ("""
   -----
   |   |
   O   |
  /|   |
       |
       |
 =========
"""),
    4: ("""
   -----
   |   |
   O   |
  /|\\  |
       |
       |
 =========
"""),
    5: ("""
   -----
   |   |
   O   |
  /|\\  |
  /    |
       |
 =========
"""),
    6: ("""
   -----
   |   |
   O   |
  /|\\  |
  / \\  |
       |
 =========
""")
}

def display_man(wrong_guesses):
    for line in hangman_art[wrong_guesses].splitlines():
        print(line)

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 1
    gussed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in gussed_letters:
            print(f"You already guessed '{guess}'. Try again.")
            continue

        gussed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess 
        else:
            wrong_guesses += 1
        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("Congratulations! You guessed the word!")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer) 
            print("Game Over!")
            is_running = False


if __name__ == "__main__":
    main()