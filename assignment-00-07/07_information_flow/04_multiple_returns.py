def get_user_data():
    first_name = input("What is your first name?: ")
    last_name = input("What is your last name?: ")
    email = input("What is your email address?: ")
    return first_name, last_name, email  # Returns as a tuple

def main():
    user_data = get_user_data()
    print("\nReceived the following user data:", user_data)

if __name__ == "__main__":
    main()