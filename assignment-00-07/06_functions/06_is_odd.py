def check_even_odd(start, end):
    for num in range(start, end + 1):
        print(f"{num} {'even' if num % 2 == 0 else 'odd'}")

check_even_odd(10, 19)  # Call the function