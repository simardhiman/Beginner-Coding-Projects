import random
import string

def generate_password(length, complexity):
    # Create a list of possible characters based on the specified complexity
    characters = []
    if complexity >= 1:
        characters += list(string.ascii_uppercase)
    if complexity >= 2:
        characters += list(string.ascii_lowercase)
    if complexity >= 3:
        characters += list(string.digits)
    if complexity >= 4:
        characters += list(string.punctuation)
    
    # Generate a random password of the specified length
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Get user input for password length and complexity
length = int(input("Enter the desired length of the password: "))
complexity = int(input("Enter the desired complexity of the password (1-4): "))

# Generate and print the password
password = generate_password(length, complexity)
print("Generated password:", password)
