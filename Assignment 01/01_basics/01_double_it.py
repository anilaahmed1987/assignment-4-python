def double_until_100():
    # Get initial number from user
    curr_value = int(input("Enter a number: "))
    
    # Double the number until it's 100 or greater
    while curr_value < 100:
        curr_value = curr_value * 2
        print(curr_value, end=' ')
    
    # Print newline at the end
    print()

if __name__ == "__main__":
    double_until_100()