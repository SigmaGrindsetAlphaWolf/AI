# Programmer: John Burke
# Date: 3/12/2024
# Program: Password Generator
# Resource: https://youtu.be/jRAAaDll34Q?si=SZq8WSYzjrmuAoIA

import hashlib
import getpass

def hash_password(password, salt):
    # Combine password and salt
    salted_password = password + salt
    # Hash the salted password using SHA-256
    hashed_password = hashlib.sha256(salted_password.encode()).hexdigest()
    return hashed_password

def main():
    # Get password from user without showing characters
    password = getpass.getpass("Enter your password: ")

    # Generate a random salt (You might want to implement a better salt generation mechanism)
    salt = "random_salt"

    # Hash the password with the salt
    hashed_password = hash_password(password, salt)

    # Print the hashed password
    print("Hashed password:", hashed_password)

if __name__ == "__main__":
    main()