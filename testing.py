# %%
user_number = ""

while user_number != "done":
    user_number = input("Enter a number (type done when finished): ")
    print(f_number(int(user_number)))
# %%
x = "sun"
y = "moon"
z = "stars"
print(x, y, z, sep="|", flush=False)
 
# %%

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
   print(number)
   numbers = 2
# %%
values = [1, 2, 3, 4, 5, 6]

for value in values:
   even_or_odd = value % 2
   print(even_or_odd)

# %%

num_even_odd = [0, 0]

print(num_even_odd)

num_even_odd[1] += 1

print(num_even_odd)


# %%

def francois(num):
    if num == 1:
        return 2
    elif num == 2:
        return 1

    # Using dynamic programming to store previously computed values
    dp = [0] * (num + 1)
    dp[1] = 2
    dp[2] = 1

    for i in range(3, num + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[num]

# Test the function
for i in range(1, 10):
    print(f"François({i}) = {francois(i)}")
# %%
