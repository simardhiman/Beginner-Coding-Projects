import random

# Generate a random number between 1 and 100
answer = random.randint(1, 100)

# Initialize number of attempts
attempts = 0

# Start the game loop
while True:
    # Get user's guess
    guess = int(input("Guess a number between 1 and 100: "))

    # Increase number of attempts
    attempts += 1

    # Check if the guess is correct
    if guess == answer:
        print("Congratulations, you guessed the number in", attempts, "attempts!")
        break
    # Check if the guess is too high
    elif guess > answer:
        print("Too high. Try again.")
    # Check if the guess is too low
    else:
        print("Too low. Try again.")
