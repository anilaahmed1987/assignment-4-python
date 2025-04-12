def sum_numbers(numbers):
    """
    This function takes a list of numbers and returns their sum.
    
    Args:
        numbers (list): A list of numbers to be summed
        
    Returns:
        float: The sum of all numbers in the list
    """
    return sum(numbers)

# Test the function
if __name__ == "__main__":
    # Example list of numbers
    test_numbers = [1, 2, 3, 4, 5]
    
    # Calculate and print the sum
    result = sum_numbers(test_numbers)
    print(f"The sum of {test_numbers} is: {result}")
