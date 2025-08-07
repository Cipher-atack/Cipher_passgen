import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%&*"
    return ''.join(random.choice(characters) for _ in range(length))

if __name__ == "__main__":
    print("🔐 Welcome to CIPHER Password Generator")
    length = int(input("Enter password length: "))
    print("Generated Password:", generate_password(length))
