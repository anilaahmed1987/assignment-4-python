def affirmation_checker():
    # Define the target affirmation
    target_affirmation = "I am capable of doing anything I put my mind to."
    
    # Print initial prompt
    print("Please type the following affirmation:", target_affirmation)
    
    while True:
        # Get user input
        user_input = input()
        
        # Check if the input matches the target affirmation
        if user_input == target_affirmation:
            print("That's right! :)")
            break
        else:
            print("Hmmm That was not the affirmation.")
            print("Please type the following affirmation:", target_affirmation)

if __name__ == "__main__":
    affirmation_checker() 