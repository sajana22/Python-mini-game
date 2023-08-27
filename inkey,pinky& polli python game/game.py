import random

# list of choices
choices = ["1", "2", "3"]

# player scores
computer_score = 0
player_score = 0

# loop until the player decides to stop
while True:
    # computer chooses a random option
    computer_choice = random.choice(choices)

    # prompt the player to choose an option
    print("Inky is stronger and more powerful than Polly")
    print("Pinky is much stronger than Inky")
    print("Inky  = 1")
    print("Pinky = 2")
    print("Polly = 3")
    player_choice = input("Enter your choice (1, 2, or 3): ")

    # check if the player entered a valid choice
    if player_choice not in choices:
        print("Invalid choice. Please try again.")
        continue

    # display the choices
    print("Player 1 chose:", "Computer player")
    print("Player 2 chose:", player_choice)

    # winner / update scores
    if computer_choice == player_choice:
        print("It's a tie. Replay!")
    elif (computer_choice == "1" and player_choice == "3") or \
         (computer_choice == "3" and player_choice == "2") or \
         (computer_choice == "2" and player_choice == "1"):
        print("Player 1 wins!")
        computer_score += 1
    else:
        print("Player 2 wins!")
        player_score += 1

    # ask the player if they want to play again
    while True:
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() == "y":
            break
        elif play_again.lower() == "n":
            print("Final scores:")
            print("Computer player:", computer_score)
            print("Your score:", player_score)
            exit()
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

    # reset the game if the player wants to play again
    if play_again.lower() == "y":
        continue
