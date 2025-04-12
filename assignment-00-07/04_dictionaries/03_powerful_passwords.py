import hashlib

def hash_password(password):
    """Hash a password using SHA256"""
    return hashlib.sha256(password.encode()).hexdigest()

def login(email, password_to_check, stored_logins):
    """
    Check if the provided password matches the stored hash for the given email
    
    Args:
        email (str): The email to check
        password_to_check (str): The password to verify
        stored_logins (dict): Dictionary of email -> password hash mappings
    
    Returns:
        bool: True if password matches, False otherwise
    """
    # Check if email exists in stored_logins
    if email not in stored_logins:
        return False
    
    # Get the stored hash for this email
    stored_hash = stored_logins[email]
    
    # Hash the password to check
    check_hash = hash_password(password_to_check)
    
    # Compare the hashes
    return stored_hash == check_hash

# Example usage
if __name__ == "__main__":
    # Example stored logins (email -> password hash)
    stored_logins = {
        "user@example.com": "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824",  # hash of "hello"
        "admin@example.com": "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"   # hash of "123456"
    }
    
    # Test the login function
    print("Testing login function:")
    print("1. Correct password:")
    print(login("user@example.com", "hello", stored_logins))  # Should return True
    
    print("\n2. Incorrect password:")
    print(login("user@example.com", "wrong", stored_logins))  # Should return False
    
    print("\n3. Non-existent email:")
    print(login("nonexistent@example.com", "hello", stored_logins))  # Should return False 