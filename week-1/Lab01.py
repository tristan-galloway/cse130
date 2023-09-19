# 1. Name: 
#    Tristan Galloway
# 2. Assignment Name: 
#    Lab 01: Python Review
# 3. Assignment Description:
#    This program will generate a random number and allow the user to guess until they get the correct numeber. It will offer feedback as they guess. It will also log how many attempts it took before getting it right.
# 4. What was the hardest part? Be as specific as possible.
#   Refactoring was the hardest part for me. I was trying to get to the point where I had the "while" loop
#   with a True condition and end the loop with the break command instead of having a variable like "win" to hold a bool condition to leave the loop once they got the right guess.
#   I was also struggling to figure out how to set up my if statement to run properly without having an exescive amount of elif statements or being too vague. 
#   Originally I had the break condition as my if statement but that left my else statement to handle either high or low guesses
#   which had a weird flow to read after the fact even though technically it worked.
# 5. How long did it take for you to complete the assignment?
#    1 hour

import random

# Game introduction.
print('This is the "guess a number" game. \nYou try to guess a random number in the smallest number of attempts.')

# Prompt the user for how difficult the game will be. Ask for an integer.
value_max = int(input("Pick a positive integer: "))

# Generate a random number between 1 and the chosen value.
value_random = random.randint(1, value_max)

# Give the user instructions as to what he or she will be doing.
print(f"Guess a number between 1 and {value_max}.")

# Initialize the sentinal and the array of guesses.
guess = 0
guesses = []

# Play the guessing game.
while True:
    # Prompt the user for a number.
    guess = int(input(""))
    # Store the number in an array so it can be displayed later.
    guesses.append(guess)
    # Make a decision: was the guess too high, too low, or just right.
    if guess < value_random:
        print("    Too low!")
    elif guess > value_random:
        print("    Too high!")
    else:
        break

# Give the user a report: How many guesses and what the guesses where.
print(f"You were able to find the number in {len(guesses)} guesses.")
print(f"The numbers you guessed were: {guesses}")

Print("test 2")