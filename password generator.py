# password_generator.py

import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    print("----------------")

    while True:
        try:
            length = int(input("Enter the desired password length (min 8): "))
            if length < 8:
                print("Password length should be at least 8 characters.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    password = generate_password(length)
    print(f"Generated Password: {password}")

if __name__ == '__main__':
    main()