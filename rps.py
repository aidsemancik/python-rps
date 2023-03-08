import random

def rps():
    # Computer Options
    actions = ["r", "p", "s"]

    # User's and Computer's Points Variables
    user_points = 0
    comp_points = 0

    # Rounds
    rounds = 1

    # Introduction - asks user what their name is
    name = input("Today we will be playing Rock, Paper, Scissors. What's your name? ")
    print("Welcome " + name + "! Let's get started!!")

    # Will play for 3 rounds unless a tie
    while rounds <= 3:
        # Will ask the player what they want to play
        user_guess = input("Rock, Paper, Scissors! (r, p, s): ")

        # The computer will decide what it wants to play
        computer_guess = random.choice(actions)

        # Adds a round being played
        rounds += 1

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
        
    if user_points > comp_points:
        print("YAY! " + name + " won with " + str(user_points) + " points! The computer had " + str(comp_points) + " points.")
    else:
        print("Aww " + name + " lost to the computer... we only had " + str(user_points) + " points and the computer had " + str(comp_points) + " points.")

    play = input("Want to play again? y/n: ")
    if play == "y":
        rps()
    else:
        print("We'll play again another time. Bye Bye!")

rps()

