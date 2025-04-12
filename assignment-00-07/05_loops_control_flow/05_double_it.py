def double_until_100():
    # Get initial number from user
    curr_value = int(input("Enter a number: "))
    
    # Double the number until it reaches or exceeds 100
    while curr_value < 100:
        curr_value = curr_value * 2
        print(curr_value, end=' ')

if __name__ == "__main__":
    double_until_100() 