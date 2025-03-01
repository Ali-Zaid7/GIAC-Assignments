# 🎮 Number Guessing Game
Welcome to the Number Guessing Game! This is a fun and simple console-based game where you get 5 attempts to guess the number correctly. The goal is to guess a randomly generated number between 50 and 100 in as few attempts as possible. 🌟

# 📝 Game Overview
🎲 Random Number: The program randomly picks a number between 50 and 100.
🔢 Your Mission: Guess the number within 5 attempts.
🔁 Feedback: The game provides helpful feedback like "too high" or "too low" after each guess to guide you closer to the right number.
🕹️ How to Play
Run the Python script.
You will be prompted to guess a number between 50 and 100.
Enter your guess and press Enter.
You will receive feedback whether your guess was too high or too low.
You have 5 attempts to guess the number. If you guess correctly, the game will celebrate your success! 🎉 If not, the correct number will be revealed after your final attempt.

# 📂 Code Snippet
```
import random

print("""
Welcome to the game! This is a number guessing game.
You get five attempts to guess the number between 50 and 100.
""")

number_to_guess = random.randrange(1, 101)
chances = 5
guess_counter = 0

while guess_counter < chances:
    guess_counter += 1
    try:
        my_guess = int(input(f"Attempt {guess_counter}: Please enter your guess: "))
    except ValueError:
        print("Please enter a valid integer.")
        guess_counter -= 1
        continue

    if my_guess == number_to_guess:
        print(f"Congratulations! The number is {number_to_guess} and you found it right in {guess_counter} attempts!")
        break
    elif my_guess > number_to_guess:
        print("Your guess is too high! Try again.")
    elif my_guess < number_to_guess:
        print("Your guess is too low! Try again.")
    
    if guess_counter == chances and my_guess != number_to_guess:
        print(f"Oops... you've used all your attempts. The correct number was {number_to_guess}. Better luck next time!")

```
# ✨ Features
User-Friendly: Simple to play with clear feedback after each guess.
Interactive: Provides real-time hints whether your guess is too high or too low.
Error Handling: Catches invalid input and prompts users to enter a valid number.

# 📈 Future Enhancements
Add a difficulty level: Easy (10 attempts), Medium (5 attempts), Hard (3 attempts).
Keep track of the high score and display it at the end of the game.
Allow multiple rounds of guessing in a single game session.

# 🤝 Contributing
If you want to contribute to this project:

Fork the repository.
Create a new branch for your feature: git checkout -b feature-branch-name
Make your changes and commit: git commit -m 'Add new feature'
Push to the branch: git push origin feature-branch-name
Create a Pull Request.

Enjoy guessing and testing your luck! 🧠🔢 Let me know if you'd like to suggest improvements or face any issues!
This is my python first project.
