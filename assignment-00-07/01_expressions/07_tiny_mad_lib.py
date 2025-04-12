# Constants
SENTENCE_START = "Code in Place is fun. I learned to program and used Python to make my"

def main():
    # Welcome message
    print("Welcome to Mad Libs!")
    print("-------------------")
    
    # Get words from user
    adjective = input("Please type an adjective and press enter. ")
    noun = input("Please type a noun and press enter. ")
    verb = input("Please type a verb and press enter. ")
    
    # Create and show the fun sentence
    print(f"\n{SENTENCE_START} {adjective} {noun} {verb}!")

if __name__ == "__main__":
    main() 