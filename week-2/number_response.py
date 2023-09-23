# %%
# Ask the user for a number.
user_num = int(input("Enter a number: "))

# Compare the users number to 10 and see if it's larger,
# equal to, or less then 10.
if user_num > 10:
    print("The number is larger then 10.")
elif user_num == 10:
    print("The number is 10!")
else:
    print("The number is less then 10.")

# %%
num_grade = int(input("Enter your grade as a number (ex 88): "))

# Define a function to display letter grades.

# If the score is greater than or equal to 90, return "A".
if num_grade >= 90:
    return "A"
# If the score is greater than or equal to 80, return "B".
elif num_grade >= 80:
    return "B"
# If the score is greater than or equal to 70, return "C".
elif num_grade >= 70:
    return "C"
# If the score is greater than or equal to 60, return "D".
elif num_grade >= 60:
    return "D"
# If the score is less than 60, return "F".
else:
    return "F"