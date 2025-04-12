# Rollercoaster height checker
MIN_HEIGHT = 50

def basic_check():
    height = float(input("How tall are you? "))
    if height >= MIN_HEIGHT:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")

def tall_enough_extension():
    while True:
        height_str = input("How tall are you? (Press Enter to quit) ")
        if height_str == "":
            break
        try:
            height = float(height_str)
            if height >= MIN_HEIGHT:
                print("You're tall enough to ride!")
            else:
                print("You're not tall enough to ride, but maybe next year!")
        except ValueError:
            print("Please enter a valid number.")

# Uncomment the function you want to run
basic_check()
# tall_enough_extension() 