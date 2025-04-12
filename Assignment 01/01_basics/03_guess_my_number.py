import random

def guess_my_number():
    # Generate random number between 0-99
    secret_number = random.randint(0, 99)
    
    while True:
        # Get user's guess
        guess = int(input("Enter a guess: "))
        
        # Check guess against secret number
        if guess > secret_number:
            print("Your guess is too high")
        elif guess < secret_number:
            print("Your guess is too low")
        else:
            print(f"Congrats! The number was: {secret_number}")
            break

if __name__ == "__main__":
    print("I am thinking of a number between 0 and 99...")
    guess_my_number()