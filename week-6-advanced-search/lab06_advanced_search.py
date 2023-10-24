# 1. Name:
#      Tristan Galloway
# 2. Assignment Name:
#      Lab 06: Advanced Search
# 3. Assignment Description:
#      It prompt the user for a filename. We will then read the contents
#      of the file into a list. The program will then prompt the user for
#      a name. Finally, we will tell the user whether the name is in the list.
# 4. Algorithmic Efficiency
#      O(n). The fastest part is the actual searching at O(log n) because as we increase
#	   n we are still splitting n in half each time we loop. So no matter how big the 
#	   the file is, it will have a relatively similar completion time. However, 
# 	   reading the file using .read makes it O(n) since it has to read each n.
# 5. What was the hardest part? Be as specific as possible.
#      Figuring out how to catch all of the weird exceptions. Like how to have a while
#	   condition that ends once we have split as much as we can. Or how to handle an
#	   empty list. Just a lot of the little things that can catch the program.
# 6. How long did it take for you to complete the assignment?
#      4 Hours.

import json

def advanced_search():

	# Ask the user for a file name
	user_file = input("File: ")

	# Try opening the user given file. 
	# If unable to locate a file with that name 
	# let the user know.
	try:
		
		#  Convert the JSON data into a list.
		with open(user_file, "r") as file:
			text = file.read()
			data = json.loads(text)

		# Get a list of words from the dictionary under the "array" key.
		words = data["array"]

		# Create a variable to hold the user given word to search for.
		search_term = input("Enter word to search for: ")

		# Initialize the start and end index.
		start_index = 0
		end_index = len(words) - 1
		middle_index = (start_index + end_index) // 2

		# If there are still terms to filter through,
		# narrow down the list.
		while start_index != end_index:
			middle_index = (start_index + end_index) // 2

			if search_term < words[middle_index]:
				end_index = middle_index - 1
			else:
				start_index = middle_index
				middle_index = (start_index + end_index) // 2

			# When the start and middle index's are equal leave the loop
			if start_index == middle_index:
				start_index = end_index

		# Let the user know if the word was found or not
		if search_term == words[end_index] or search_term == words[middle_index]:
			return print("\nTerm was found.")
		else:
			return print("\nTerm was not found.")

	# If the file can't be found or it's empty, put an error on screen
	# for the user.
	except FileNotFoundError:
		print(f'\nSorry but we were unable to find the file {user_file}\n')
	except IndexError:
		print("The list provided was empty.")

advanced_search()