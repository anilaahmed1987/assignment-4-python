# Simulate rolling two dice, three times. Prints the results of each die roll. 
# This program is used to show how variable scope works.

# Global variable to keep track of total rolls
import random


total_rolls = 0

def roll_dice():
    # Local variables for each roll 
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1, die2

def main():
    import random
    
    # Using global variable
    global total_rolls
    
    print("Rolling two dice three times:")
    print("-" * 30)
    
    for i in range(3):
        # Local variables from roll_dice function
        die1, die2 = roll_dice()
        total_rolls += 1
        
        print(f"Roll {i + 1}:")
        print(f"Die 1: {die1}")
        print(f"Die 2: {die2}")
        print(f"Sum: {die1 + die2}")
        print("-" * 30)
    
    # Demonstrating global variable scope
    print(f"Total number of rolls: {total_rolls}")

if __name__ == '__main__':
    main()