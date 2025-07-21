

# Prompt the user to enter a positive integer for the pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop to iterate through rows
while row < size:
    # Use a for loop to print asterisks in a row
    for _ in range(size):
        print("*", end="")  # Print without a newline
    print()  # Move to the next line after each row
    row += 1
