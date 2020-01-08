# Course: CS 30
# Period: 1
# Date created: 19/11/15
# Date last modified: 20/01/08
# Name: Mingyuan Lin
# Description: print out the inventory you have and gain

# Inventory and characteristics

# This is the inventory of the items you have when you start the game

# item_have = {
#     'Phone': {
#         'Description': 'This is the only item you have when you woke up',
#         'Condition': 'With only 2% battery and no WIFI signal',
#         'Usage': 'You can use to contact and watch YouTube if you find WIFI',
#         },
#     }


# This is the inventory of the tools you gain as you play the game

# tool_gain = {
#     'Cross key': {
#         'Description': 'This is a key shaped as a cross',
#         'Condition': 'Other than the shape, there is nothing special '
#         'about the key',
#         'Usage': 'It can only open the specific lock',
#         },
#     'Journal': {
#         'Description': 'This is the journal from some else',
#         'Condition': 'The trace left on the journal showed that '
#         'the owner have written on it everyday',
#         'Usage': 'Maybe you can learn some information about the situation '
#         'you are involved in',
#         },
#     'Gold key': {
#         'Description': 'This is a gold key',
#         'Condition': 'It is just a key that is colored in gold, not that '
#         'the material is gold',
#         'Usage': 'You can use to open a lock, it is not used for you to '
#         'sell it for money',
#         },
#     'Paper strip': {
#         'Description': 'This is a strip made out of paper',
#         'Condition': 'It belonged to a notebook, you can easily come up '
#         'with the solution by the rough edge of the strip',
#         'Usage': 'Some werid notes has written on it, maybe it is the key'
#         'to a mistery or maybe it is just some sketch',
#         },
#     }


# def print_items():
#     """print the inventory with the item you have and gain"""
#     print("\nInventory of the items you have:")
#     for item, item_info in item_have.items():
#         print(f"* {item}:")
#         for thing, info in item_info.items():
#             print(f"\t{thing}: {info}.")

#     print("\nInventory of the tools you gain:")
#     for tool, tool_info in tool_gain.items():
#         print(f"* {tool}:")
#         for sub, des in tool_info.items():
#             print(f"\t{sub}: {des}.")


class ItemHave:
    def __str__(self):
        return self.name


class Phone(ItemHave):
    def __init__(self):
        self.name = 'Phone'
        self.description = 'This is the only item you have when you woke up.'
        self.condition = 'With only 2% battery and no WIFI signal.'
        self.usage = 'You can use to contact and watch YouTube '
        'if you find WIFI.'


class ToolGain:
    def __str__(self):
        return self.name


class Crosskey(ToolGain):
    def __init__(self):
        self.name = 'Cross key'
        self.description = 'This is a key shaped as a cross.'
        self.condition = 'Other than the shape, there is nothing special '
        'about the key.'
        self.usage = 'It can only open the specific lock.'


class Journal(ToolGain):
    def __init__(self):
        self.name = 'Journal'
        self.description = 'This is the journal from some else.'
        self.condition = 'The trace left on the journal showed that '
        'the owner have written on it everyday.'
        self.usage = 'Maybe you can learn some information about the '
        'situation you are involved in.'


class GoldKey(ToolGain):
    def __init__(self):
        self.name = 'Gold key'
        self.description = 'This is a gold key.'
        self.condition = 'It is just a key that is colored in gold, not that '
        'the material is gold.'
        self.usage = 'You can use to open a lock, it is not used for you to '
        'sell it for money.'


class PaperStrip(ToolGain):
    def __init__(self):
        self.name = 'Paper strip'
        self.description = 'This is a strip made out of paper.'
        self.condition = 'It belonged to a notebook, you can easily come up '
        'with the solution by the rough edge of the strip.'
        self.usage = 'Some werid notes has written on it, maybe it is the key '
        'to a mistery or maybe it is just some sketch.'
