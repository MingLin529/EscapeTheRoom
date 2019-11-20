# Course: CS 30
# Period: 1
# Date created: 19/11/15
# Date last modified:
# Name: Mingyuan Lin
# Description: print out the inventory you have and gain

# Inventory and characteristics

# This is the inventory of the items you have when you start the game

item_have = {
    'Phone': {
        'Description': 'This is the only item you have when you woke up',
        'Condition': 'With only 2% battery and no WIFI signal',
        'Usage': 'You can use to contact and watch YouTube if you find WIFI',
        },
    }


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


def print_items():
    """print the inventory with the item you have and gain"""
    print("\nInventory of the items you have:")
    for item, item_info in item_have.items():
        print(f"* {item}:")
        for thing, info in item_info.items():
            print(f"\t{thing}: {info}.")

    print("\nInventory of the tools you gain:")
    for tool, tool_info in tool_gain.items():
        print(f"* {tool}:")
        for sub, des in tool_info.items():
            print(f"\t{sub}: {des}.")
