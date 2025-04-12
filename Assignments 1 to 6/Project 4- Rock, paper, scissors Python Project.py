# MagicHandsGame.py
import random

print("""
🪨📄✂️ MAGIC HANDS BATTLE ✂️📄🪨
Welcome to the Rock Paper Scissors Arena!
Beat the computer 3 times to become champion! 🏆
""")

wins = 0
rounds = 0

while wins < 3 and rounds < 5:
    # Player choice with emoji display
    print("\nChoose your weapon:")
    player = input("[1] Rock 🪨\n[2] Paper 📄\n[3] Scissors ✂️\n>>> ").lower()
    
    # Computer choice
    computer = random.choice(["rock", "paper", "scissors"])
    
    # Input validation
    if player not in ["1", "2", "3", "rock", "paper", "scissors"]:
        print("🚨 Oops! Please choose 1/2/3 or type the weapon name!")
        continue
    
    # Convert number input to text
    if player == "1": player = "rock"
    elif player == "2": player = "paper"
    elif player == "3": player = "scissors"
    
    # Showdown animation
    print(f"\n⚡ YOU: {player.capitalize()}  vs  COMPUTER: {computer.capitalize()} ⚡")
    
    # Battle logic
    if player == computer:
        print("✨ It's a tie! Both chose same!")
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        wins += 1
        print(f"🎉 You win! {player.capitalize()} beats {computer}!")
    else:
        print(f"😢 Computer wins! {computer.capitalize()} beats {player}!")
    
    rounds += 1
    print(f"Score: You {wins} | Computer {rounds - wins - (player==computer)}\n")
    print("-"*40)

# Final result
if wins >= 3:
    print("""
🌟🌟🌟 CHAMPION! 🌟🌟🌟
You won 3 times! Here's your trophy:
       ___________
      '._==_==_=_.'
      .-\:      /-.
     | (|:.     |) |
      '-|:.     |-'
        \::.    /
         '::. .'
           ) (
          _.' '._
         """)
else:
    print("""
💪 Nice try! Better luck next time!
Practice makes perfect! Keep playing!
""")

print("Thanks for playing! 👋")
1