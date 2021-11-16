from random import randint

#list of play options
t = ["Rock", "Paper", "Scissors"]

#assign random play to a computer
computer = t[randint(0,2)]

#set player to false
player = False

while player == False:
    #set player
    player = input("Rock, Paper, Scissors?")
    if player == computer:
        print("Tie")
    elif player == "Rock":
        if computer == "Paper":
            print("You loose", computer, "covers", player)
        else:
            print("You win", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You loose", computer, "cut", player)
        else:
            print("You win", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You loose", computer, "smashes", player)
        else:
            print("You win", player, "cut", computer)
    else:
        print("This is not valid play")

    player = False
    computer = t[randint(0,2)]