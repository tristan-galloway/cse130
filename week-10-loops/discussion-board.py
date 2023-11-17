user_number = int(input("Number: "))
user_range = range(1, user_number + 1)

for number in user_range:
    sq_number = 2 ** number
    print(sq_number)