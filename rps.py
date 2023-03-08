import random

actions = ["Rock", "Paper", "Scissors"]

user_points = 0
comp_points = 0

rounds = 1

while rounds <= 3:
    user_guess = input("Rock, Paper, Scissors!")

    computer_guess = random.choice(actions)

    rounds += 1

    if user_guess == computer_guess:
        print("Oops! We guessed the same number. Lets go again!")
        rounds -= 1
        continue
    elif user_guess == "Rock" and computer_guess == "Scissors":
        user_points += 1
        print("Haha! Rock beats Scissors, point for user!")
    elif user_guess == "Paper" and computer_guess == "Rock":
        user_points += 1
        print("Haha! Paper beats Rock, point for user!")
    elif user_guess == "Scissors" and computer_guess == "Paper":
        user_points += 1
        print("Haha! Scissors beats Paper, point for user!")
    elif user_guess == "Scissors" and computer_guess == "Rock":
        comp_points += 1
        print("Aww... Rock beats Scissors, point for computer!")
    elif user_guess == "Rock" and computer_guess == "Paper":
        comp_points += 1
        print("Aww... Paper beats Rock, point for computer!")
    elif user_guess == "Paper" and computer_guess == "Scissors":
        comp_points += 1
        print("Aww... Scissors beats Paper, point for computer!")
    
if user_points > comp_points:
    print("YAY! We won with " + str(user_points) + " points!")
else:
    print("Aww we lost to the computer... we had " + str(user_points) + " points and the computer had " + str(comp_points) + " points.")

# commit1
