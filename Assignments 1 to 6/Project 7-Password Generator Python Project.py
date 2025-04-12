# SecretCodeGuardian.py
import random

print("""
🔐🔒 SECRET CODE GUARDIAN 🔒🔐
Create super-strong passwords that even hackers can't crack!
""")

def check_password(password):
    score = 0
    feedback = []
    
    # Length check
    if len(password) >= 8:
        score += 1
        feedback.append("✅ Good length!")
    else:
        feedback.append("❌ Too short - needs 8+ characters")
    
    # Uppercase check
    if any(char.isupper() for char in password):
        score += 1
        feedback.append("✅ Great! Uppercase letters")
    else:
        feedback.append("❌ Add CAPITAL letters")
    
    # Number check
    if any(char.isdigit() for char in password):
        score += 1
        feedback.append("✅ Awesome numbers!")
    else:
        feedback.append("❌ Needs secret numbers")
    
    # Special character check
    special_chars = "!@#$%^&*"
    if any(char in special_chars for char in password):
        score += 1
        feedback.append("✅ Cool symbols!")
    else:
        feedback.append("❌ Add special symbols like ! or #")
    
    return score, feedback

def generate_password():
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*"
    return ''.join(random.choices(characters, k=10))

while True:
    print("\nChoose an action:")
    choice = input("[1] Check my password\n[2] Make new password\n[3] Exit\n>>> ")
    
    if choice == "1":
        user_pass = input("\nEnter your secret code: ")
        strength, tips = check_password(user_pass)
        
        print("\n🔍 Password Report:")
        print("\n".join(tips))
        print(f"\nSecurity Power: {'★' * strength}{'☆' * (4 - strength)}")
        
        if strength == 4:
            print("""
            🏆 SUPER SECURE! 🏆
            You're a password wizard!
               .-""-.    .-""-.
              /      \../      \\
              \      /""\      /
               '.__.'    '.__.'
            """)
            
    elif choice == "2":
        new_pass = generate_password()
        print(f"\n✨ Your new magic code: {new_pass}")
        print("Copy it somewhere safe!")
        
    elif choice == "3":
        print("\nThanks for being a security hero! 👋")
        break
        
    else:
        print("\n🛑 Oops! Choose 1, 2 or 3")

