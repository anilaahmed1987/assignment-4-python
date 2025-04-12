def subtract_seven(num):
    """Subtracts 7 from the given number"""
    return num - 7

def main():
    # Get user input
    number = float(input("Enter a number: "))
    
    # Call the helper function
    result = subtract_seven(number)
    
    # Print the result
    print(f"{number} minus 7 is {result}")

if __name__ == "__main__":
    main()