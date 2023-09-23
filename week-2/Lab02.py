# 1. Name:
#      Tristan Galloway
# 2. Assignment Name:
#      Lab 02: Authentication
# 3. Assignment Description:
#      Compare a user-given username and password and cross referrence agaisn't a
#      file with a list of valid username/password combinations
# 4. What was the hardest part? Be as specific as possible.
#      The problem that took me the longest to figure out was how to iterate through the list
#      and return 1 time whether or not the login attempt was successful. I originally told the
#      user within the for loop, but if it was correct it would say it was correct once at the top
#      then repeatedly say that they failed. I solved it after about 15 minutes of trial running what was going wrong.
# 5. How long did it take for you to complete the assignment?
#      1.75 Hours

import json

# Try to open the Lab02.json file, if the computer can't open it,
# explain to the user the error
try:
    #  Convert the JSON data into a list.
    with open("Lab02.json", "r") as file:
        text = file.read()
        data = json.loads(text)

        # Get a list of usernames from the dictionary under the "username" key.
        usernames = data["username"]
        passwords = data["password"]

        # Create variables to hold the user given username and password then set the sentinal.
        given_username = input("Username: ")
        given_password = input("Password: ")
        authentication = False

        # Iterate through the usernames and see if the given username is the same,
        # if it is, check the same index in passwords and check if it matches 
        # the given password. If it matches set authentication to true.
        for i, user in enumerate(usernames):
            if given_username == user and given_password == passwords[i]:
                authentication = True
            else:
                i += 1
        
        # Let the user know whether or not they were authenticated
        if authentication == True:
            print("\nYou are authenticated!\n")
        else:
            print("\nYou are not authorized to use the system.\n")

# If the file isn't found, let the user know why.
except FileNotFoundError:
    print("\nUnable to find the file Lab02.json.\n")
except:
    print("\nSome other exception occurred.\n")