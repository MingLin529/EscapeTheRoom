# Course: CS 30
# Period: 1
# Date created: 19/10/03
# Date last modified:
# Name: Mingyuan Lin
# Description:

# Main game file

# Characters and traits

# This is the character you are going to be in the game, some informations
# are given

print("This is the traits of the character:")
characters = {
    'John': {
        'First name': 'John',
        'Last name': 'Anderson',
        'Identity': 'college student',
        },
    }

for character, character_info in characters.items():
    print(f"Character: {character}")
    full_name = f"{character_info['First name']} {character_info['Last name']}"
    identity = character_info['Identity']

    print(f"\tHe's full name is {full_name}, and he is a {identity}. "
          "\n\tUnfortunately, he is the only and main character in this game. "
          "\n\tYou are not expecting him to have super powers, right?")

# Locations and descriptions

# These are the rooms you are going to go throw in the game

locations = {
    'Room 1': {
        'Description': 'is the guest room and the starting room',
        },
    'Room 2': {
        'Description': 'is the master room',
        },
    'Room 3': {
        'Description': 'is the living room',
        },
    'Room 4': {
        'Description': 'is the basement',
        },
    }

print("\nThese are the locations you are going to investe in the house:")
for room, room_info in locations.items():
    description = room_info['Description']

    print(f"\t{room} {description}.")

# Inventory and characteristics

# This is the inventory of the items you have when you start the game

item_have = {
    'Phone': {
        'Description': 'This is the only item you have when you woke up',
        'Condition': 'With only 2% battery and no WIFI signal',
        'Usage': 'You can use to contact and watch YouTube if you find WIFI',
        },
    }

print("\nInventory of the items you have:")
for item, item_info in item_have.items():
    print(f"* {item}:")
    for thing, info in item_info.items():
        print(f"\t{thing}: {info}.")

# This is the inventory of the tools you gain as you play the game

tool_gain = {
    'Cross key': {
        'Description': 'This is a key shaped as a cross',
        'Condition': 'Other than the shape, there is nothing special '
        'about the key',
        'Usage': 'It can only open the specific lock',
        },
    'Journal': {
        'Description': 'This is the journal from some else',
        'Condition': 'The trace left on the journal showed that '
        'the owner have written on it everyday',
        'Usage': 'Maybe you can learn some information about the situation '
        'you are involved in',
        },
    'Gold key': {
        'Description': 'This is a gold key',
        'Condition': 'It is just a key that is colored in gold, not that '
        'the material is gold',
        'Usage': 'You can use to open a lock, it is not used for you to '
        'sell it for money',
        },
    'Paper strip': {
        'Description': 'This is a strip made out of paper',
        'Condition': 'It belonged to a notebook, you can easily come up '
        'with the solution by the rough edge of the strip',
        'Usage': 'Some werid notes has written on it, maybe it is the key'
        'to a mistery or maybe it is just some sketch',
        },
    }

print("\nInventory of the tools you gain:")
for tool, tool_info in tool_gain.items():
    print(f"* {tool}:")
    for sub, des in tool_info.items():
        print(f"\t{sub}: {des}.")
