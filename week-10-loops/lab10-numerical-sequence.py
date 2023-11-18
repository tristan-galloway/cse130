# 1. Name:
#      Tristan Galloway
# 2. Assignment Name:
#      Lab 10: Numeric Sequence
# 3. Assignment Description:
#      This program takes a user given number, and computes what that number would be
#      In francois counting system.
# 4. What was the hardest part? Be as specific as possible.
#      I think for me it's still the asserts. I went back and watched the supplemental
#      videos on asserts where you explained that they aren't supposed to catch user 
#      errors but instead catch errors of future coding changes to the function I think
#      helped me understand the way we are supposed to be using them.
# 5. How long did it take for you to complete the assignment?
#      It took about 3 hours. I'm not totally sure since it was very split up because I
#      am taking care of my fiance. She just got her tonsils removed, so my work flow was 
#      very scattered over the last few days.

def main():

    # Set the user_number variable so it will run the first time.
    user_number = 0

    # Continue asking for a number while the given number is a non positive integer.
    while user_number <= 0:
        user_number = int(input("Enter a number: "))

    # Initialize the numbers list to house two locations to store values.
    numbers = [1, 2] #[1%2]=[1] and [2%2]=[0]
    assert numbers == [1, 2]

    # Alternate the location to combine the numbers in slot one and two
    # in the list numbers.
    if user_number > 2:
        assert user_number > 2
        for i in range(3, user_number + 1):
            numbers[i % 2] = numbers[0] + numbers[1]

    # Set the value as the higher of the two that was last added to.
    value = numbers[user_number % 2]

    # Value should be a positive number
    assert value >= 0

    # Print the users number in francois counting system.
    return print(f"\nFracois number is {value}")

# If the program is imported, ignore the call to main.
if __name__ == "__main__":
    main()