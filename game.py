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
