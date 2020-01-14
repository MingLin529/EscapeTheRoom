# Course: CS 30
# Period: 1
# Date created: 19/10/03
# Date last modified: 20/01/12
# Name: Mingyuan Lin
# Description:

# Main game file

# import the module of map, character and plot
import character
from map import ViewMap
from plot import StartingPlot
from plot import WatchYoutube
from plot import SearchForWiFi
from plot import TurnOnLowBatteryMode
from plot import TurnOffThePhone
from plot import Transition1
from plot import LeaveTheHair
from plot import Transition2
from plot import LayBackToBed1
from plot import LockTheDoor
from plot import TakeTheBlackHair
from plot import LayBackToBed2
from plot import JumpDownTheWindow


# Instructions to follow

prompt = "\nEnter a number in front of the directions: "
prompt += "\n(Enter 0 when you want to quit game.)"

prompt2 = "\nEnter 1 or 2: "
prompt2 += "\n(Enter 0 to return to start scene.)"

# the choice of directions you have
directions = ['Start Game',
              'Map',
              'Character']

directions2 = ['search for wifi',
               'watch YouTube']

directions3 = ['turn on low battery mode to save battery',
               'turn off the phone to save battery']

directions4 = ['leave the hair',
               'take the black hair with you']

directions5 = ['lay back to bed',
               'lock the door']

directions6 = ['flip through the window to next door',
               'jump down the window']


def actions():
    """loop out the choise from dictionary with its index"""
    for direction in directions:
        print(f"{directions.index(direction)+1}. {direction}")


def actions2():
    """loop out the choise from dictionary with its index"""
    for direction in directions2:
        print(f"{directions2.index(direction)+1}. {direction}")


def actions3():
    """loop out the choise from dictionary with its index"""
    for direction in directions3:
        print(f"{directions3.index(direction)+1}. {direction}")


def actions4():
    """loop out the choise from dictionary with its index"""
    for direction in directions4:
        print(f"{directions4.index(direction)+1}. {direction}")


def actions5():
    """loop out the choise from dictionary with its index"""
    for direction in directions5:
        print(f"{directions5.index(direction)+1}. {direction}")


def actions6():
    """loop out the choise from dictionary with its index"""
    for direction in directions6:
        print(f"{directions6.index(direction)+1}. {direction}")


def choice():
    """the very last exception handling"""
    while True:
        try:
            plot5 = int(input(f"{prompt2}\n"))
        except ValueError:
            print("The input is not a number, please try agian!\n")
        else:
            if plot5 == 0:
                print("\n")
                choice6()  # return to start scene
            elif plot5 == 1:
                print("\nTo Be Continued...")
            elif plot5 == 2:
                jump = JumpDownTheWindow()
                print(f"\n{jump}")
                print("\nEnd 4-You died (Found by the dog)\n")
                choice6()  # return to start scene
            else:
                print("\nThis number is INVALID. Please choose "
                      "another number.\n")


def choice1():
    """the second last exception handling"""
    while True:
        try:
            plot4 = int(input(f"{prompt2}\n"))
        except ValueError:
            print("The input is not a number, please try agian!\n")
        else:
            if plot4 == 0:
                print("\n")
                choice6()  # return to start scene
            elif plot4 == 1:
                lay_2 = LayBackToBed2()
                print(f"\n{lay_2}")
                print("\nEnd 3-You died(You pretended asleep after you took "
                      "something? Wake up!)\n")
                choice6()  # return to start scene
            elif plot4 == 2:
                lock_door = LockTheDoor()
                print(f"\n{lock_door}\n")
                actions6()
                choice()
            else:
                print("\nThis number is INVALID. Please choose another "
                      "number.\n")


def choice2():
    """the third last exception handling"""
    while True:
        try:
            plot3 = int(input(f"{prompt2}\n"))
        except ValueError:
            print("The input is not a number, please try agian!\n")
        else:
            if plot3 == 0:
                print("\n")
                choice6()  # return to start scene
            elif plot3 == 1:
                lay_1 = LayBackToBed1()
                print(f"\n{lay_1}")
                print("\nEnd 2-Is it a dream?\n")
                choice6()  # return to start scene
            elif plot3 == 2:
                lock_door = LockTheDoor()
                print(f"\n{lock_door}\n")
                actions6()
                choice()
            else:
                print("\nThis number is INVALID. Please choose another "
                      "number.\n")


def choice3():
    """the third exception handling"""
    while True:
        try:
            plot2 = int(input(f"{prompt2}\n"))
        except ValueError:
            print("The input is not a number, please try agian!\n")
        else:
            if plot2 == 0:
                print("\n")
                choice6()  # return to start scene
            elif plot2 == 1:
                leave_the_hair = LeaveTheHair()
                print(f"\n{leave_the_hair}")
                transition_2 = Transition2()
                print(f"{transition_2}\n")
                actions5()
                choice2()
            elif plot2 == 2:
                take_hair = TakeTheBlackHair()
                print(f"\n{take_hair}")
                transition_2 = Transition2()
                print(f"{transition_2}\n")
                actions5()
                choice1()
            else:
                print("\nThis number is INVALID. Please choose another "
                      "number.\n")


def choice4():
    """the second exception handling"""
    while True:
        try:
            plot = int(input(f"{prompt2}\n"))
        except ValueError:
            print("The input is not a number, please try agian!\n")
        else:
            if plot == 0:
                print("\n")
                choice6()  # return to start scene
            elif plot == 1:
                low_battery = TurnOnLowBatteryMode()
                print(f"\n{low_battery}")
                transition_1 = Transition1()
                print(f"{transition_1}\n")
                actions4()
                choice3()
            elif plot == 2:
                turn_off = TurnOffThePhone()
                print(f"\n{turn_off}")
                transition_1 = Transition1()
                print(f"{transition_1}\n")
                actions4()
                choice3()
            else:
                print("\nThis number is INVALID. Please choose another "
                      "number.\n")


def choice5():
    """the first exception handling"""
    while True:
        try:
            start = int(input(f"{prompt2}\n"))
        except ValueError:
            print("The input is not a number, please try agian!\n")
        else:
            if start == 0:
                print("\n")
                choice6()  # return to start scene
            elif start == 1:
                search_ForWiFi = SearchForWiFi()
                print(f"\n{search_ForWiFi}\n")
                actions3()
                choice4()
            elif start == 2:
                watch_youtube = WatchYoutube()
                print(f"\n{watch_youtube}")
                print("\nEnd 1-You died(Sounds too loud!)\n")
                choice6()  # return to start scene
            else:
                print("\nThis number is INVALID. Please choose another "
                      "number.\n")


# keep looping while the input is not 0. When its 0, the loop quit
def choice6():
    """the start scene of the game"""
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
                starting_plot = StartingPlot()
                print(f"\n{starting_plot}\n")
                actions2()
                choice5()
            elif name == 2:
                view_map = ViewMap()
                view_map.print_house()
            elif name == 3:
                print("\n")
                character.print_character()
                print("\n")
            else:
                print("\nThis number is INVALID. Please choose another "
                      "number.\n")

# Run the game
choice6()
