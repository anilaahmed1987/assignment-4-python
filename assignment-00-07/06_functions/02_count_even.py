def count_even(lst):
    """
    Counts and returns the number of even numbers in the given list.
    
    Args:
        lst (list): List of integers to check
        
    Returns:
        int: Number of even numbers in the list
    """
    count = 0
    for num in lst:
        if num % 2 == 0:
            count += 1
    return count

def main():
    # First part: populate the list
    numbers = []
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":
            break
        try:
            num = int(user_input)
            numbers.append(num)
        except ValueError:
            print("Please enter a valid integer or press enter to stop.")
    
    # Second part: count and print even numbers
    even_count = count_even(numbers)
    print(f"There are {even_count} even numbers in the list.")

if __name__ == "__main__":
    main() 