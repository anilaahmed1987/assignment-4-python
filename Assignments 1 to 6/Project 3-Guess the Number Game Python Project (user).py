# NumberExplorer.py
import random

print("""
🚀🌌 SPACE NUMBER CHALLENGE 🌌🚀
Aliens hid a secret number between 1-50!
Find it in 10 tries to power the rocket! ✨
""")

while True:
    secret_num = random.randint(1, 50)
    attempts = 0
    score = 100  # Start with perfect score
    
    while attempts < 10:
        try:
            guess = int(input(f"\n🌠 Attempt {attempts+1}/10: Your guess (1-50)? "))
            
            if guess < 1 or guess > 50:
                print("⚠️ Only numbers between 1-50!")
                continue
                
            attempts += 1
            score -= 10  # Deduct 10 points per try
            
            if guess == secret_num:
                print(f"""
🎉 SUCCESS! You found {secret_num} in {attempts} {'try' if attempts==1 else 'tries'}!
🏆 Final Score: {max(score, 0)}/100
🚀 Rocket boosters activated! Ready for launch! 🌍➡️🌕
""")
                break
            else:
                # Progressive hints system
                difference = abs(guess - secret_num)
                if attempts >= 5:
                    hint = "EVEN" if secret_num%2 ==0 else "ODD"
                    print(f"💡 Hint: It's an {hint} number!")
                elif attempts >= 3:
                    print("🌡️ Getting warmer!" if difference <=10 else "❄️ Getting colder!")
                
                # Direction guidance
                print("⬆️ Go higher!" if guess < secret_num else "⬇️ Go lower!")
                
        except ValueError:
            print("🛑 Please enter numbers only (e.g., 5 or 27)")
    
    else:
        print(f"""
😢 Oh no! The secret number was {secret_num}
🔧 Repairing rocket... Try again! 🛠️
""")
    
    # Play again option
    restart = input("\nPlay again? (yes/no): ").lower()
    if restart not in ['yes', 'y']:
        print("\nThanks for playing! 👨🚀👩🚀")
        break
