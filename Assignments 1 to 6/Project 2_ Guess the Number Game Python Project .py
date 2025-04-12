# magic_number_game.py

import random

print("""
✨🔢 MAGIC NUMBER GAME 🔢✨

Hi Explorer! 🧑🚀
I'm thinking of a secret number between 1-20.
Can you guess it in 7 tries? 🌈
""")

secret_number = random.randint(1, 20)
guesses = 0

while True:
    try:
        guess = int(input("\n🌻 Your guess (1-20): "))
        guesses += 1
        
        if guess < 1 or guess > 20:
            print("🚧 Oops! Only numbers 1-20 please!")
            continue
            
        if guess < secret_number:
            print("🔺 Try higher! The magic number is bigger!")
        elif guess > secret_number:
            print("🔻 Go lower! The magic number is smaller!")
        else:
            print(f"""
🎉 YOU DID IT! 🎉
The magic number was {secret_number}! 
You found it in {guesses} {'try' if guesses ==1 else 'tries'}!
""")
            break
            
        if guesses == 4:
            print("\n💡 Halfway there! Keep going!")
        elif guesses == 7:
            print(f"""
😢 Game Over! The number was {secret_number}.
You'll get it next time! 💪
""")
            break
            
    except ValueError:
        print("📛 That's not a number! Use digits like 5 or 12")

print("\nThanks for playing! 👋 Come back soon!")
