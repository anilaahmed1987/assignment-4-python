import random

def main():
    # Welcome message
    print("Dice Roller")
    print("-----------")
    
    # Roll first die
    die1 = random.randint(1, 6)
    print(f"First die: {die1}")
    
    # Roll second die
    die2 = random.randint(1, 6)
    print(f"Second die: {die2}")
    
    # Calculate and show total
    total = die1 + die2
    print(f"Total: {total}")

if __name__ == "__main__":
    main() 