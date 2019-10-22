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
character = {
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

tool_gain = {
'Cross key': {
'Description': '', 
'Condition': '',
'Usage': '',
},
'Journal': {
'Description': '',
'Condition': '',
'Usage': '',
},
'Gold key': {
'Description': '',
'Condition': '',
'Usage': '',
},
'Paper strip': {
'Description': '',
'Condition': '',
'Usage': '',
},
}
