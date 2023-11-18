# %%
user_number = int(input("Number: "))
user_range = range(1, user_number + 1)

for number in user_range:
    sq_number = 2 ** number
    print(sq_number)


# %%
acc_balances = [1500, 20000, 15000, -200000, -2000, -25000]
net_worth = 0

for balance in acc_balances:
    net_worth += balance

# %%
