# Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural.

# Constants
INCHES_PER_FOOT = 12

def main():
    # Step 1: Welcome message
    print("Feet to Inches Converter")
    print("-----------------------")
    
    # Step 2: Get input from user
    feet = float(input("Enter number of feet: "))
    
    # Step 3: Calculate inches
    inches = feet * INCHES_PER_FOOT
    
    # Step 4: Show the result
    print(f"\n{feet} feet = {inches} inches")

if __name__ == "__main__":
    main()

