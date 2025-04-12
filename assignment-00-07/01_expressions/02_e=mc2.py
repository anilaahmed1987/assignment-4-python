# Constants
SPEED_OF_LIGHT = 299792458  # m/s

def main():
    # Welcome message
    print("Einstein's Energy Calculator")
    print("E = m * c²")
    print("---------------------------")
    
    # Get mass from user
    mass = float(input("Enter kilos of mass: "))
    
    # Calculate energy
    energy = mass * (SPEED_OF_LIGHT ** 2)
    
    # Show calculation and result
    print("\ne = m * C^2...")
    print(f"m = {mass} kg")
    print(f"C = {SPEED_OF_LIGHT} m/s")
    print(f"{energy} joules of energy!")

if __name__ == "__main__":
    main() 