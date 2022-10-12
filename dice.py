import random
print("*** Dice Generator ***")

print("You can throw the dice what if write ''throw''")
x = input()
numbers = ("1","2","3","4","5","6")
computer_number = random.choice(numbers)
if x == ("throw") and computer_number == ("1"):
    print("-----------")
    print("|         |")
    print("|    o    |")
    print("|         |")
    print("-----------")

elif x == ("throw") and computer_number == ("2"):
    print("-----------")
    print("|      o  |")
    print("|         |")
    print("|  o      |")
    print("-----------")

elif x == ("throw") and computer_number == ("3"):
    print("-----------")
    print("|       o |")
    print("|    o    |")
    print("| o       |")
    print("-----------")

elif x == ("throw") and computer_number == ("4"):
    print("------------")
    print("|  o    o  |")
    print("|          |")
    print("|  o    o  |")
    print("------------")

elif x == ("throw") and computer_number == ("5"):
    print("-------------")
    print("|  o     o  |")
    print("|     o     |")
    print("|  o     o  |")
    print("-------------")

elif x == ("throw") and computer_number == ("6"):
    print("------------")
    print("|  o    o  |")
    print("|  o    o  |")
    print("|  o    o  |")
    print("------------")

else:
    print("Please write right!")


