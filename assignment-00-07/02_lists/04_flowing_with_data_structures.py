def add_three_copies(lst, data):
    """
    Adds three copies of the data to the list.
    This demonstrates mutability since the list is modified in place.
    
    Args:
        lst (list): The list to modify
        data: The data to add three copies of
    """
    lst.append(data)
    lst.append(data)
    lst.append(data)

def main():
    # Get user input
    message = input("Enter a message to copy: ")
    
    # Create an empty list
    my_list = []
    
    # Show the list before modification
    print(f"\nList before: {my_list}")
    
    # Add three copies of the message to the list
    add_three_copies(my_list, message)
    
    # Show the list after modification
    print(f"List after: {my_list}")

if __name__ == "__main__":
    main() 