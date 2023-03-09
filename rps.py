import random

def rps():
    # List of computer Options
    actions = ["r", "p", "s"]

    # Variables for user's and computer's Points
    user_points = 0
    comp_points = 0

    # Variable for number of rounds
    rounds = 1

    # Introduction - asks user what their name is
    name = input("Today we will be playing Rock, Paper, Scissors. What's your name? ")
    print("Welcome " + name + "! Let's get started!!")

    # While the rounds are less than or equal to 3 the game will be played
    while rounds <= 3:
        # User input to ask what their move is
        user_guess = input("Rock, Paper, Scissors! (r, p, s): ")

        # Random function to allow the computer to pick a move
        computer_guess = random.choice(actions)

        # Adds a round played to the rounds variable
        rounds += 1

        # If/Else statement to determine whether the user or computer receives a point
        if user_guess == computer_guess:
            print("Oops! We guessed the same move. Lets go again!")
            rounds -= 1
            continue
        elif user_guess == "r" and computer_guess == "s":
            user_points += 1
            print("Haha! Rock beats Scissors, point for " + name + "!")
        elif user_guess == "p" and computer_guess == "r":
            user_points += 1
            print("Haha! Paper beats Rock, point for " + name + "!")
        elif user_guess == "s" and computer_guess == "p":
            user_points += 1
            print("Haha! Scissors beats Paper, point for " + name + "!")
        elif user_guess == "s" and computer_guess == "r":
            comp_points += 1
            print("Aww... Rock beats Scissors, point for computer!")
        elif user_guess == "r" and computer_guess == "p":
            comp_points += 1
            print("Aww... Paper beats Rock, point for computer!")
        elif user_guess == "p" and computer_guess == "s":
            comp_points += 1
            print("Aww... Scissors beats Paper, point for computer!")

    # If/Else statement to determines if the user won or lost 
    if user_points > comp_points:
        print("YAY! " + name + " won with " + str(user_points) + " points! The computer had " + str(comp_points) + " points.")
    else:
        print("Aww " + name + " lost to the computer... we only had " + str(user_points) + " points and the computer had " + str(comp_points) + " points.")

    # Asks the user if they would like to play again with an If/Else statement
    play = input("Want to play again? y/n: ")
    if play == "y":
        rps()
    else:
        print("We'll play again another time. Bye Bye!")

# Starts the game
rps()




# Clear Terminal
# 1. nano ~/.bash_profile
# 2. export PS1="\$ "
# 3. source ~/.bash_profile
# Use the source command every time terminal is started, undo changes once complete


