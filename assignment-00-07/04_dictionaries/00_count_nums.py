def count_numbers():
    # Initialize an empty dictionary to store number counts
    number_counts = {}
    
    # Get numbers from user until they enter a non-number
    while True:
        try:
            num = input("Enter a number: ")
            if not num:  # If user just presses Enter, break the loop
                break
            num = int(num)
            
            # Update the count in the dictionary
            if num in number_counts:
                number_counts[num] += 1
            else:
                number_counts[num] = 1
        except ValueError:
            break
    
    # Print the results
    for num, count in sorted(number_counts.items()):
        print(f"{num} appears {count} times.")

if __name__ == "__main__":
    count_numbers()