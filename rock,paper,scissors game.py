import random

option = ("rock", "paper", "scissors")
running = True
computer_wins = 0
player_wins = 0
tie = 0

while running:

    
    player = None
    computer = random.choice(option)

    while player not in option:
        player = input("Choose between rock, paper, scissors: ").lower()

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    
    if player == computer:
        print("Tie")
        tie += 1
    elif player == "rock" and computer == "paper":
        print("You lost!")
        computer_wins += 1
    elif player == "rock" and computer == "scissors":
        print("You won!")
        player_wins += 1
    elif player == "paper" and computer == "scissors":
        print("You lost!")
        computer_wins += 1
    elif player == "paper" and computer == "rock":
        print("You won!")
        player_wins += 1
    elif player == "scissors" and computer == "rock":
        print("You lost!")
        computer_wins += 1
    else:
        print("You won!")
        player_wins += 1

    print(f"PLayer win: {player_wins}")
    print(f"Computer win: {computer_wins}")
    print(f"Tie: {tie}")

    if player_wins == 3:
        print("You won!")
        running = False
    elif computer_wins == 3:
        print("Computer won!")
        break
    if not input("DO you want to continue(y/n): ").lower() == "y":
        running = False