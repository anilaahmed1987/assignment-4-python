def fruit_shop():
    # Dictionary of fruits and their prices
    fruits = {
        'apple': 2.5,
        'durian': 15.0,
        'jackfruit': 20.0,
        'kiwi': 3.0,
        'rambutan': 5.0,
        'mango': 4.0
    }
    
    total_cost = 0.0
    
    # Loop through each fruit and ask for quantity
    for fruit, price in fruits.items():
        while True:
            try:
                quantity = int(input(f"How many ({fruit}) do you want?: "))
                if quantity >= 0:
                    break
                print("Please enter a non-negative number.")
            except ValueError:
                print("Please enter a valid number.")
        
        # Calculate cost for this fruit and add to total
        total_cost += quantity * price
    
    # Print the total cost
    print(f"\nYour total is ${total_cost:.1f}")

if __name__ == "__main__":
    fruit_shop() 