# 1. Name:
#      Tristan Galloway
# 2. Assignment Name:
#      Lab 10: Numeric Sequence
# 3. Assignment Description:
#      This program takes a user given number, and computes what that number would be
#      In francois counting system.
# 4. What was the hardest part? Be as specific as possible.
#      -a paragraph or two about how the assignment went for you-
# 5. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the program-

import time

def main():
    """Runs the following test cases and prints the results as it goes.
    (-1, 0, 1, 2, 9, 100, 200)
    """
    
    user_number = ""

    while user_number != "done":
        user_number = input("Enter a number (type done when finished): ")
        print(f_number(int(user_number)))

def f_number(user_number):
    pass