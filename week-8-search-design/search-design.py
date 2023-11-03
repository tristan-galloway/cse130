# 1. Name:
#      Tristan Galloway
# 2. Assignment Name:
#      Lab 08: Sort
# 3. Assignment Description:
#      Take a JSON file from a user and sort it alphabetically.
# 4. What was the hardest part? Be as specific as possible.
#      Figuring out what asserts would be useful and what would just be redunant.
#      I had to look up a lot of ideas and figure out the technical way to code my concepts.abs
#      Like I know where I'm getting a user input would be a good place to add an assert. But
#      I wasn't sure how to make a valid boolean statement to check that the user gave a valid 
#      file name.
# 5. How long did it take for you to complete the assignment?
#      2 Hours

import json
import os

# Ask the user for a file name
user_file = input("File: ")

# Verify if the file exists
assert os.path.exists(user_file)

# Try opening the user given file. 
# If unable to locate a file with that name 
# let the user know.
try:
    # Convert the JSON data into a list.
    with open(user_file, "r") as file:
        text = file.read()
        data = json.loads(text)
    
    # Verify if "array" key exists in the loaded JSON data
    assert "array" in data

    # Get a list of words from the dictionary under the "array" key.
    words = data["array"]

    # Initialize the pivot point as the last item in the list
    i_pivot = len(words) - 1

    # Run until the first item in the list is reached.
    while i_pivot > 0:

        # Initialize the largest value index variable.
        i_largest = 0

        # Iterate through the words list prior to the pivot point.
        for i_check, item in enumerate(words[: i_pivot]):

            # If the word we are checking is greater then the largest 
            # word so far, update the largest index.
            if words[i_check] > words[i_largest]:
                i_largest = i_check

        # If the largest word found prior to the word at i_pivot, 
        # swap the values.
        if words[i_largest] > words[i_pivot]:
            words[i_pivot], words[i_largest] = words[i_largest], words[i_pivot]

        # Shift the pivot one index earlier
        i_pivot -= 1

    # Verify if the list is sorted
    assert words == sorted(words)

    # If the list has items, print them. If the list was empty 
    # let the user know.
    if len(words) > 0:
        # Iterate through the list and print the values in their new order.
        print(f"The values in {user_file} are:")
        for word in words:
            print(f"    {word}")
    else:
        print("The list didn't have any items")

# If the file can't be found or it's empty, put an error on screen
# for the user.
except FileNotFoundError:
    print(f'\nSorry but we were unable to find the file {user_file}\n')