import random

def print_random_numbers():
    # Generate and print 10 random numbers between 1 and 100
    for _ in range(10):
        print(random.randint(1, 100), end=' ')
    print()  # Add a newline at the end

if __name__ == "__main__":
    print_random_numbers()