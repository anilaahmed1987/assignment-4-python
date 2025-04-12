def access_element(lst, index):
    """Access an element at the specified index"""
    try:
        return lst[index]
    except IndexError:
        return "Index out of range!"

def modify_element(lst, index, new_value):
    """Modify an element at the specified index"""
    try:
        lst[index] = new_value
        return f"Updated list: {lst}"
    except IndexError:
        return "Index out of range - cannot modify!"

def slice_list(lst, start, end):
    """Return a slice of the list from start to end index"""
    try:
        return lst[start:end]
    except IndexError:
        return "Invalid indices for slicing!"

def list_game():
    # Initialize a sample list
    my_list = [10, 20, 30, 40, 50, 'apple', 'banana', 'cherry']
    
    print("Welcome to the List Practice Game!")
    print(f"Starting list: {my_list}\n")
    
    while True:
        print("\nMenu:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            # Access operation
            index = int(input(f"Enter index (0-{len(my_list)-1}): "))
            result = access_element(my_list, index)
            print(f"\nElement at index {index}: {result}")
            
        elif choice == '2':
            # Modify operation
            index = int(input(f"Enter index (0-{len(my_list)-1}): "))
            new_value = input("Enter new value: ")
            try:
                new_value = int(new_value)
            except ValueError:
                pass  # Keep as string if not a number
            result = modify_element(my_list, index, new_value)
            print(f"\n{result}")
            
        elif choice == '3':
            # Slice operation
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            result = slice_list(my_list, start, end)
            print(f"\nSlice from {start} to {end}: {result}")
            
        elif choice == '4':
            print("\nThanks for playing!")
            break
            
        else:
            print("Invalid choice. Please try again.")
        
        # Show current list after each operation
        print(f"\nCurrent list: {my_list}")

if __name__ == "__main__":
    list_game()