
user = input("Enter 'rock', 'paper', or 'scissors' for player 1: ").lower()
user2 = input("Enter 'rock', 'paper', or 'scissors' for player 2: ").lower()

if user == user2:
    print("Draw!")
elif user not in ("rock", "paper", "scissors") or user2 not in ("rock", "paper", "scissors"):
    print("Invalid input! Please enter 'rock', 'paper', or 'scissors'.")
elif (user == "rock" and user2 == "scissors") or \
     (user == "paper" and user2 == "rock") or \
     (user == "scissors" and user2 == "paper"):
    print("Winner: Player 1")
else:
    print("Winner: Player 2")
