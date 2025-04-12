import random

NUM_ROUNDS = 3

def play_round(round_num, score):
    print(f"\nRound {round_num}")
    # Generate numbers
    user_num = random.randint(1, 100)
    computer_num = random.randint(1, 100)
    print(f"Your number is {user_num}")
    
    # Get valid user input
    while True:
        guess = input("Do you think your number is higher or lower than the computer's?: ").lower()
        if guess in ['higher', 'lower']:
            break
        print("Please enter either higher or lower")
    
    # Determine result
    if (guess == 'higher' and user_num > computer_num) or (guess == 'lower' and user_num < computer_num):
        print(f"You were right! The computer's number was {computer_num}")
        score += 1
    else:
        print(f"Sorry! The computer's number was {computer_num}")
    
    print(f"Your score is now {score}")
    return score

def play_game():
    print("Welcome to the High-Low Game!")
    score = 0
    
    for round_num in range(1, NUM_ROUNDS + 1):
        score = play_round(round_num, score)
    
    # Final evaluation
    print("\nGame over!")
    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    play_game()