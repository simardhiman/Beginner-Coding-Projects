import random

def play_game(player1, player2):
    # Possible choices
    choices = ["rock", "paper", "scissors"]
    # Get player1's choice
    if player1 == "computer":
        player1_choice = random.choice(choices)
    else:
        player1_choice = input(f"{player1}, choose rock, paper, or scissors: ").lower()
    # Get player2's choice
    if player2 == "computer":
        player2_choice = random.choice(choices)
    else:
        player2_choice = input(f"{player2}, choose rock, paper, or scissors: ").lower()
    # Compare choices and determine winner
    if player1_choice == player2_choice:
        return "It's a tie!"
    elif (player1_choice == "rock" and player2_choice == "scissors") or (player1_choice == "paper" and player2_choice == "rock") or (player1_choice == "scissors" and player2_choice == "paper"):
        return f"{player1} wins with {player1_choice}!"
    else:
        return f"{player2} wins with {player2_choice}!"

while True:
    # Get number of players
    players = int(input("Enter number of players (1 or 2): "))
    if players == 1:
        player1 = input("Enter your name: ")
        print(play_game(player1, "computer"))
    elif players == 2:
        player1 = input("Player 1, enter your name: ")
        player2 = input("Player 2, enter your name: ")
        print(play_game(player1, player2))
    else:
        print("Invalid number of players.")
