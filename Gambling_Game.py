import random
import time

def roll_dice():
    """Simulate rolling a dice with a fun animation"""
    print("\nRolling the dice...")
    time.sleep(0.5)
    print("  _______ ")
    print(" /       \\")
    print(f"|    {random.randint(1, 6)}    |")
    print(" \\_______/")
    time.sleep(0.5)

def play_game():
    print("""
    WELCOME TO THE DICE GAME!
    =========================
    Rules:
    1. Take turns rolling a 6-sided die
    2. If you roll 2-6, add it to your score
    3. If you roll 1, you lose your turn's points
    4. First player to reach 30 points wins!
    """)
    
    # Get number of players (2-4)
    while True:
        players = input("How many players? (2-4): ")
        if players.isdigit() and 2 <= int(players) <= 4:
            players = int(players)
            break
        print("Please enter 2, 3, or 4!")
    
    scores = [0] * players  # Create score list
    
    while True:
        for player in range(players):
            print(f"\nPlayer {player+1}'s turn!")
            print(f"Current score: {scores[player]}")
            input("Press Enter to roll...")
            
            # Roll the dice
            roll = random.randint(1, 6)
            roll_dice()  # Show dice animation
            print(f"You rolled a {roll}!")
            
            if roll == 1:
                print("Oh no! You lose your turn's points!")
                turn_score = 0
            else:
                turn_score = roll
                print(f"You gained {roll} points this turn!")
            
            scores[player] += turn_score
            print(f"Your total score is now: {scores[player]}")
            
            # Check for winner
            if scores[player] >= 30:
                print(f"\nPlayer {player+1} wins with {scores[player]} points!")
                print("GAME OVER!")
                return

# Start the game
play_game()