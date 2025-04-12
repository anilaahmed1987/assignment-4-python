# TimeWizard.py
import time
import sys

def countdown(seconds):
    print("\n🔮✨ Let the countdown begin! ✨🔮")
    for t in range(seconds, -1, -1):
        mins, secs = divmod(t, 60)
        timer = f"⏳ {mins:02d}:{secs:02d} "
        
        # Progress bar visualization
        progress = '#' * (seconds - t) + '_' * t
        progress_bar = f"[{progress.ljust(seconds)}]"
        
        # Time-based messages
        if t == 0:
            print("\n🎉🎊 TIME'S UP! 🎊🎉")
            print("""
            __
           /  \\ 
          /|oo \\ 
         (_|  /_)
          _`@/_ \\    _
         |     | \\   \\
         | (*) |  \\   ) 
         ʤ______/____/  
            """)
        elif t <= 5:
            print(f"{timer} 🔥 Almost there! {progress_bar}")
        else:
            print(f"{timer} {'⭐' * (t%3 + 1)} {progress_bar}")
        
        time.sleep(1)

def main():
    print("""
🌈🌈🌈 WELCOME TO TIME WIZARD! 🌈🌈🌈
Create your magic timer (1-99 seconds):
""")
    
    while True:
        try:
            duration = int(input("Enter seconds: "))
            if 1 <= duration <= 99:
                countdown(duration)
                break
            else:
                print("🚨 Please enter between 1-99 seconds!")
        except ValueError:
            print("🛑 Numbers only please! (e.g., 10)")
    
    # Restart option
    if input("\nMake another timer? (yes/no): ").lower() in ['yes', 'y']:
        main()
    else:
        print("\nThanks for time traveling! ⏰✨")

if __name__ == "__main__":
    main()
