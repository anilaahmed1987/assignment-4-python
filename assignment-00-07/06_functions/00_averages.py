def calculate_average(num1, num2):
    """
    Calculate the average of two numbers.
    
    Args:
        num1 (float): First number
        num2 (float): Second number
        
    Returns:
        float: The average of the two numbers
    """
    return (num1 + num2) / 2

# Example usage
if __name__ == "__main__":
    # Test the function
    number1 = 10
    number2 = 20
    result = calculate_average(number1, number2)
    print(f"The average of {number1} and {number2} is {result}") 