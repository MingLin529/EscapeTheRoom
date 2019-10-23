# Course: CS 30
# Period: 1
# Date created: 19/10/03
# Date last modified:
# Name: Mingyuan Lin
# Description:

# Main game file

# list of what you start with
item_have = ['phone']
# list of what you gain
tool_gain = []

# tools that are added to inventory2
tool_gain.append('cross key')
tool_gain.insert(1, 'journal')
tool_gain.insert(2, 'gold key')
tool_gain.insert(3, 'paper strip')

# print out the catergory for list of item have
print(f"The items you have:")
for item in item_have:
    # code adopted from Seungyeon Moon
    print(f"{item_have.index(item)+1}. {item}")

# print out the catergory for list of tool gain
print(f"The tools you gain:")
for tool in tool_gain:
    print(f"{tool_gain.index(tool)+1}. {tool}")


# character and traits
characters = {
    'John': {
        'First name': 'John',
        'Last name': 'Anderson',
        'Identity': 'College Student',
        },
    }

# locations and descriptions

locations = {
    'Room 1': {
        'Description': 'It is the guest room and the starting room',
        },
    'Room 2': {
        'Decription': 'It is the master room',
        },
    'Room 3': {
        'Decription': 'It is the living room',
        },
    'Room 4': {
        'Decription': 'It is the basement',
        },
    }

# inventory and characteristics

item_have = {
    'Phone': {
        'Description': 'This is the only item you have when you woke up',
        'Condition': 'With only 2% battery and no WIFI signal',
        'Usage': 'You can use to contact and watch YouTube if you find WIFI',
        },
    }

tool_gain = []

tool_1 = {
    'Cross key': {
        'Description': 'This is a key shaped as a cross',
        'Condition': 'Other than the shape, there is nothing special '
        'about the key',
        'Usage': 'It can only open the specific lock',
        },
    }

tool_2 = {
    'Journal': {
        'Description': 'This is the journal from some else',
        'Condition': 'The trace left on the journal showed that '
        'the owner have written on it everyday',
        'Usage': 'Maybe you can learn some information about the situation '
        'you are involved in',
        },
    }

tool_3 = {
    'Gold key': {
        'Description': 'This is a gold key',
        'Condition': 'It is just a key that is colored in gold, not that '
        'the material is gold',
        'Usage': 'You can use to open a lock, it is not used for you to '
        'sell it for money',
        },
    }

tool_4 = {
    'Paper strip': {
        'Description': 'This is a strip made out of paper',
        'Condition': 'It belonged to a notebook, you can easily come up '
        'with the solution by the rough edge of the strip',
        'Usage': 'Some werid notes has written on it, maybe it is the key'
        'to a mistery or maybe it is just some sketch',
        },
    }

tool_gain.append(tool_1)
tool_gain.insert(1, tool_2)
tool_gain.insert(2, tool_3)
tool_gain.insert(3, tool_4)
