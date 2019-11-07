# Course: CS 30
# Period: 1
# Date created: 19/10/29
# Date last modified: 19/11/07
# Name: Mingyuan Lin
# Description: a simple menu for the player to follow and make choices


# the choice of directions you have

directions = ['flip through the window to next door',
              'jump down the window',
              'head straight downstairs']

# Instructions to follow

prompt = "\nEnter a number in front of the directions you want to go: "
prompt += "\n(Enter 0 when you are stopping.)"


def actions():
    """loop out the choise from dictionary with its index"""
    for direction in directions:
        print(f"{directions.index(direction)+1}. {direction}")


# keep looping while the input is not 0. When its 0, the loop quit

while True:
    actions()

    name = int(input(f"{prompt}\n"))

    if name == 0:
        break
    elif name == 1:
        print(f"\nYou {directions[0]}.\n")
    elif name == 2:
        print(f"\nYou {directions[1]}.\n")
    elif name == 3:
        print(f"\nYou {directions[2]}.\n")
    else:
        print("\nThis number is INVALID. Please choose another number.\n")
