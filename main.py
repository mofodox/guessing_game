import random
import time

print("Welcome to the Number Guessing Game!\n====================================")
print("Let's start the game. I will think of a number between 1 and 10, and you have to guess it.")

time.sleep(3)
print("Picking a number...")
time.sleep(2)

guess = int(input("Guess a number between 1 and 10: "))
correct_number = random.randint(1, 10)
guess_count = 0

while guess != correct_number:
    time.sleep(1)
    guess_count += 1
    if guess < correct_number:
        print("Too low! Try again.")
        guess = int(input("Guess a number between 1 and 10: "))
    else:
        print("Too high! Try again.")
        guess = int(input("Guess a number between 1 and 10: "))

print(f"Yay! You guessed the correct number {correct_number}! It took you {guess_count} guesses.")