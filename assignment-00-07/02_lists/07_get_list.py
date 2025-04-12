def main():
    # Initialize an empty list
    values = []
    
    # Continuously ask for input until empty input is received
    while True:
        value = input("Enter a value: ")
        
        # If the input is empty (user just pressed enter), break the loop
        if value == "":
            break
            
        # Add the value to the list
        values.append(value)
    
    # Print the final list
    print(f"Here's the list: {values}")

if __name__ == "__main__":
    main() 