import random


def play():
    while True:
        player = input('What is your choice?\n "r" for rock "p" for paper "s" for scissors ')
        computer = random.choice(["r", "p", "s"])
        if player == computer:
            print("It's a tie")
        else:
            if is_win(player, computer):
                print("You have won!")
            else:
                print("Sorry, you lost")


def is_win(player, opponent):
    if (
        (player == "r" and opponent == "s")
        or (player == "s" and opponent == "p")
        or (player == "p" and opponent == "r")
    ):
        return True
play()