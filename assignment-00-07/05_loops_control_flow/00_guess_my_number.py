import random

def guess_my_number():
    # Generate a random number between 0 and 99
    secret_number = random.randint(0, 99)
    
    print("I am thinking of a number between 0 and 99...")
    
    while True:
        try:
            # Get player's guess
            guess = int(input("Enter a guess: "))
            
            # Check if guess is too high, too low, or correct
            if guess > secret_number:
                print("Your guess is too high")
            elif guess < secret_number:
                print("Your guess is too low")
            else:
                print(f"Congrats! The number was: {secret_number}")
                break
                
        except ValueError:
            print("Please enter a valid number between 0 and 99")

if __name__ == "__main__":
    guess_my_number()
