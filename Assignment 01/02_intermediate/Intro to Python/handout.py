def calculate_planet_weight():
    # Planet gravity constants (compared to Earth)
    planet_gravity = {
        'Mercury': 0.376,
        'Venus': 0.889,
        'Mars': 0.378,
        'Jupiter': 2.36,
        'Saturn': 1.081,
        'Uranus': 0.815,
        'Neptune': 1.140
    }
    
    # Get user input
    earth_weight = float(input("Enter your weight on Earth (kg): "))
    planet = input("Enter a planet (Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune): ")
    
    # Calculate and display weight
    if planet in planet_gravity:
        planet_weight = earth_weight * planet_gravity[planet]
        print(f"Your weight on {planet} would be: {round(planet_weight, 2)} kg")
    else:
        print("Invalid planet name entered.")

if __name__ == "__main__":
    calculate_planet_weight()