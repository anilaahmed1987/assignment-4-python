def double_numbers(numbers):
    """
    This function takes a list of numbers and returns a new list with each number doubled.
    
    Args:
        numbers (list): A list of numbers to be doubled
        
    Returns:
        list: A new list with each number doubled
    """
    return [num * 2 for num in numbers]

# Test the function
if __name__ == "__main__":
    # Example list of numbers
    numbers = [1, 2, 3, 4]
    
    # Double the numbers
    doubled_numbers = double_numbers(numbers)
    
    # Print the results
    print(f"Original numbers: {numbers}")
    print(f"Doubled numbers: {doubled_numbers}") 