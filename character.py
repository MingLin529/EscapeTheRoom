# Course: CS 30
# Period: 1
# Date created: 19/11/15
# Date last modified:
# Name: Mingyuan Lin
# Description: layout the character you are

# Characters and traits

# This is the character you are going to be in the game, some informations
# are given

characters = {
    'John': {
        'First name': 'John',
        'Last name': 'Anderson',
        'Identity': 'college student',
        },
    }


def print_character():
    """print out the character you are"""
    print("This is the traits of the character:")
    for character, info in characters.items():
        print(f"Character: {character}")
        full_name = f"{info['First name']} {info['Last name']}"
        identity = info['Identity']

        print(f"\tHe's full name is {full_name}, and he is a {identity}. "
              "\n\tUnfortunately, he is the only and main character " +
              "in this game. "
              "\n\tYou are not expecting him to have super powers, right?")
