def get_last_element(lst):
    """
    Prints the last element of the given list.
    
    Args:
        lst (list): A non-empty list
    """
    print(f"The last element is: {lst[-1]}")

def main():
    # Initialize an empty list
    my_list = []
    
    # Get the number of elements from the user
    num_elements = int(input("How many elements do you want in your list? "))
    
    # Get each element from the user
    for i in range(num_elements):
        element = input(f"Enter element {i + 1}: ")
        my_list.append(element)
    
    # Print the last element
    get_last_element(my_list)

if __name__ == "__main__":
    main()
