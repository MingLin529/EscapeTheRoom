# Course: CS 30
# Period: 1
# Date created: 19/10/29
# Date last modified: 19/10/30
# Name: Mingyuan Lin
# Description: a simple menu for the player to follow and make choices


# the choice of directions you have

directions = ['flip through the window to next door',
             'jump down the window',
             'head straight downstairs']

# print out the question and choices

print("Which direction are you taking? (print out the number)")
for direction in directions:
    print(f"{directions.index(direction)+1}. {direction}")

# print out a specific choice when you entered an input

name = int(input("Enter choice: "))
if name == 1:
    print(f"\n{directions[0]}")
elif name == 2:
    print(f"\n{directions[1]}")
else:
    print(f"\n{directions[2]}")
