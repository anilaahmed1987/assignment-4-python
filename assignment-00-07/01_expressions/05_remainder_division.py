# Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.

# Here's a sample run of the program (user input is in bold italics):

# Please enter an integer to be divided: 5

# Please enter an integer to divide by: 3

# The result of this division is 1 with a remainder of 2



def main():
    # Welcome message
    print("Division Calculator")
    print("-----------------")
    
    # Get first number
    num1 = int(input("Please enter an integer to be divided: "))
    
    # Get second number
    num2 = int(input("Please enter an integer to divide by: "))
    
    # Calculate division and remainder
    result = num1 // num2  # Integer division
    remainder = num1 % num2  # Remainder
    
    # Show result
    print(f"\nThe result of this division is {result} with a remainder of {remainder}")

if __name__ == "__main__":
    main()
