import random

choices = {
    "s": "scissors",
    "p": "paper",
    "r": "rock"
}

def get_player_choice():
    choice = input("Choose scissors (s), paper (p), or rock (r): ").lower()
    while choice not in choices:
        choice = input("Invalid choice. Please choose scissors (s), paper (p), or rock (r): ").lower()
    return choices[choice]

def play_game():
    player_choice = get_player_choice()
    computer_choice = random.choice(list(choices.values()))
    print(f"Computer chose {computer_choice}.")
    if player_choice == computer_choice:
        print("It's a tie!")
    elif player_choice == "scissors" and computer_choice == "paper":
        print("You win!")
    elif player_choice == "paper" and computer_choice == "rock":
        print("You win!")
    elif player_choice == "rock" and computer_choice == "scissors":
        print("You win!")
    else:
        print("Computer wins!")

while True:
    play_game()
    again = input("Do you want to play again? (y/n): ")
    if again.lower() != "y":
        break
