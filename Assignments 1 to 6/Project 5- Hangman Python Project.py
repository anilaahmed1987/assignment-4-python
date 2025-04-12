# CrypticHangman.py
import random
import sys

HANGMAN_STAGES = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''']

WORD_CATEGORIES = {
    "SCIENCE": [
        "electromagnetic", "photosynthesis", 
        "crystallography", "biotechnology",
        "paleontology", "nanotechnology"
    ],
    "LITERATURE": [
        "onomatopoeia", "personification",
        "metaphorical", "alliteration",
        "epistemology", "postmodernism"
    ],
    "GEOGRAPHY": [
        "archipelago", "cartography",
        "topography", "demographics",
        "meteorology", "seismograph"
    ]
}

def select_word(category):
    return random.choice(WORD_CATEGORIES[category]).upper()

def display_word(word, guessed):
    return ' '.join([letter if letter in guessed else '_' for letter in word])

def calculate_score(lives_remaining, word_length, hints_used):
    return (lives_remaining * 15) + (word_length * 5) - (hints_used * 20)

def game():
    print("""
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓   CRYPTIC HANGMAN CHALLENGE ▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
""")
    
    # Game setup
    category = input("Choose category [Science/Literature/Geography]: ").upper()
    while category not in WORD_CATEGORIES:
        category = input("Invalid category! Choose from Science/Literature/Geography: ").upper()
    
    secret_word = select_word(category)
    guessed_letters = set()
    lives = 6
    hints = 2
    score = 0

    print(f"\nCategory: {category.title()}")
    print(f"Word Length: {len(secret_word)} letters")
    print(HANGMAN_STAGES[0])

    while lives > 0:
        print("\n" + display_word(secret_word, guessed_letters))
        print(f"Lives: {lives} | Hints: {hints} | Guessed: {' '.join(sorted(guessed_letters))}")
        
        try:
            guess = input("Enter letter or 'hint': ").upper()
            
            if guess == "HINT":
                if hints > 0:
                    unhinted = [l for l in secret_word if l not in guessed_letters]
                    reveal = random.choice(unhinted)
                    guessed_letters.add(reveal)
                    hints -= 1
                    print(f"Hint: Letter '{reveal}' revealed!")
                else:
                    print("No hints remaining!")
                continue
                
            if not guess.isalpha() or len(guess) != 1:
                raise ValueError
                
            if guess in guessed_letters:
                print("Already guessed! Try again.")
                continue
                
            guessed_letters.add(guess)
            
            if guess not in secret_word:
                lives -= 1
                print(f"Incorrect! {HANGMAN_STAGES[6 - lives]}")
            else:
                print("Correct!")
                
            if all(letter in guessed_letters for letter in secret_word):
                score = calculate_score(lives, len(secret_word), 2 - hints)
                print(f"""
╔════════════════════════╗
║       VICTORY!         ║
║  The word was: {secret_word:<10}║
║  Final Score: {score:<5}       ║
╚════════════════════════╝
""")
                return
                
        except ValueError:
            print("Invalid input! Enter single letters only.")

    print(f"""
╔════════════════════════╗
║      GAME OVER!        ║
║  The word was: {secret_word:<10}║
╚════════════════════════╝
""")

if __name__ == "__main__":
    while True:
        game()
        if input("\nPlay again? (y/n): ").lower() != 'y':
            sys.exit("Thanks for playing! Goodbye!")
