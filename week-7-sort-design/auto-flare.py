# Prompt for grade
number = int(input("Please enter a positive number: "))

# Initialize sum
sum = 0
print(f"Base sum: {sum}")

# Count it up
for count in range(1, number):
    print(f"\nCount: {count}")
    print(f"Sum: {sum}")
    sum += count
    print(f"Count + Sum: {sum}")

# Report
print(f"\nThe sum is:", sum)