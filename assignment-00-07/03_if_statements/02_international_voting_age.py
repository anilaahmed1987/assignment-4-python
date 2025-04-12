# Voting age checker for three fictional countries
age = int(input("How old are you? "))

# Check voting eligibility for each country
if age >= 16:
    print(f"You can vote in Pakistan where the voting age is 16.")
else:
    print(f"You cannot vote in Pakistan where the voting age is 16.")

if age >= 25:
    print(f"You can vote in Japan where the voting age is 25.")
else:
    print(f"You cannot vote in Japan where the voting age is 25.")

if age >= 48:
    print(f"You can vote in china where the voting age is 48.")
else:
    print(f"You cannot vote in china where the voting age is 48.") 