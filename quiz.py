# Simple Quiz Game

questions = (
    "What is the capital of France?",
    "Which planet is known as Red Planet?",
    "What is 2 + 2?"
)

options = (
    ("A. Paris", "B. London", "C. Rome", "D. Berlin"),
    ("A. Earth", "B. Mars", "C. Jupiter", "D. Venus"),
    ("A. 3", "B. 4", "C. 5", "D. 6")
)

answers = ("A", "B", "B")

guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------")
    print(question)
    
    for option in options[question_num]:
        print(option)
        
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Wrong!")
    
    question_num += 1

print("----------------------")
print("RESULTS")
print("Score:", score, "/", len(questions))