import random

print("It is Rock Paper Scissors")
print("Make a choose in rock,paper and scissors")

possible_actions = ["rock","paper","scissors"]
player_action = input()
computer_action = random.choice(possible_actions)

print("You choose " + player_action, "and computer choose " +computer_action)

if player_action == computer_action:
    print("Draw")

elif player_action == ("rock") and computer_action == ("paper"):
    print("Computer won")

elif player_action == ("rock") and computer_action == ("scissors"):
    print("Player won")

elif player_action == ("paper") and computer_action == ("rock"):
    print("Player won")

elif player_action == ("paper") and computer_action ==("scissors"):
    print("Computer won")

elif player_action == ("scissors") and computer_action ==("paper"):
    print("Player won")

elif player_action == ("scissors") and computer_action ==("rock"):
    print("Computer won")



