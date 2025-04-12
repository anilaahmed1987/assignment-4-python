def num_in_stock(fruit):
    # Sophia's inventory dictionary
    inventory = {
        'apple': 50,
        'banana': 75,
        'pear': 1000,
        'orange': 120,
        'kiwi': 30
    }
    return inventory.get(fruit.lower(), 0)  # Returns 0 if fruit not found

def main():
    fruit = input("Enter a fruit: ")
    quantity = num_in_stock(fruit)
    
    if quantity > 0:
        print("This fruit is in stock! Here is how many:")
        print(quantity)
    else:
        print("This fruit is not in stock.")

if __name__ == "__main__":
    main()