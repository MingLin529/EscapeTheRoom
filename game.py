# Course: CS 30
# Period: 1
# Date created: 19/10/03
# Date last modified:
# Name: Mingyuan Lin
# Description:

# Main game file

# import the module of map, character, and inventory
# from map import ViewMap
# import character
# from inventory import Phone

# print out the module
# print("Here is the map of the house: ")
# view_map = ViewMap()
# view_map.print_house()

# a blanc line to separate the two parts

# character.print_character()

# leave a blanc line to separate the parts
# print("\n")

# print out the item you have
# phone = Phone()
# print(f"You have your {phone} to start with!")

# leave a blanc line to separate the parts
# print("\n")

# the choice of directions you have

# directions = ['flip through the window to next door',
#              'jump down the window',
#              'head straight downstairs']

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
    try:
        name = int(input(f"{prompt}\n"))
    except ValueError:
        print("The input is not a number, please try agian!\n")
    else:
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
