import random

user_input = input("Enter a choice : (rock , paper , scissors)")
possible_actions = ["rock","paper","scissors"]
computer_actions = random.choice(possible_actions)
if user_input == computer_actions:
    print("Tie")
elif user_input == "rock":
    if computer_actions == "paper":
        print("computer wins")
    else:
        print("User wins")
elif user_input == "rock":
    if computer_actions == "scissors":
        print("user wins")
    else:
        print("computer wins")
elif user_input == "scissors":
    if computer_actions == "paper":
        print("User wins")
    else:
        print("computer wins")

    

#print user action and computer action
