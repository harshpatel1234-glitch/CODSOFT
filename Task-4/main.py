# SIMPLE GAME ROCK, PAPER, SCISSORS

import random


user_input = input("enter rock, paper, or scissors: ").lower()
choose_option = random.choice(['rock', 'paper', 'scissors'])
print(f"The computer chose: {choose_option}")


if user_input == choose_option:
    print("It's a tie!")
elif user_input == "rock":
    if choose_option == "scissors":
        print("You win! Rock crushes scissors.")
    else:
        print("You lose!")
elif user_input == "paper":
    if choose_option == "rock":
        print("You win! Paper covers rock.")
    else:
        print("You lose!")
elif user_input == "scissors":
    if choose_option == "paper":
        print("You win! Scissors cut paper.")
    else:
        print("You lose!")
play_again = input("Do you want to play again? (yes/no): ").lower()
if play_again == "yes":
    import os
    os.system('python main.py') # Restart the game 
else:
    print("Thanks for playing!")    