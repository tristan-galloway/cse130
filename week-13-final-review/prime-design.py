# 1. Name:
#      Tristan Galloway
# 2. Assignment Name:
#      Lab 13: Prime Numbers
# 3. Assignment Description:
#      This program will display all the prime numbers at or below a certain value. 
#      It will first prompt the user for an integer. If the integer is less than 2,
#      then the program will prompt the user for another number. The program will 
#      then compute all the prime numbers below (and including) the given number. 
#      When finished, the program will display the list of prime numbers.
# 4. What was the hardest part? Be as specific as possible.
#      The hardest part was figuring out why my placement in the lists was off. I 
#      had the equation right at first on line 38 but forgot to account for the 
#      way the computer was indexing at line 36 by adding an extra 1. I also still
#      struggle with adding asserts but I feel like I did better this time. I 
#      understand better that it's to check for computational issues or coding issues
#      not to catch user input errors.
# 5. How long did it take for you to complete the assignment?
#      4 Hours

import math

# Get the user number to find primes below.
number = int(input("This program will find all the prime numbers at or below N. Select that N: "))
assert isinstance(number, int)
assert number >= 2, "Please Enter a number larger then 2."


# Set an array with True values for each number leading up to the user number.
numbers = [True] * (number + 1)
assert len(numbers) == len(range(1, number + 2))

# Set the first two values as false
numbers[0] = numbers[1] = False
assert numbers[0] == False
assert numbers[1] == False

# For each number below the square root user number, cross off each multiple of that number.
for factor in range(2, round(math.sqrt(number)) + 2):
    if numbers[factor]:
        assert numbers[factor] == True
        for multiple in range(factor * 2, number + 1, factor):
            numbers[multiple] = False

# Initialize the list to hold the list of prime numbers
primes = []

# Iterate through the numbers list and put the true values in a list.
for index in range(2, number + 1):
    if numbers[index]:
        primes.append(index)

# Return the prime numbers below the users number.
print(primes)