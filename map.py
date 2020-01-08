# Course: CS 30
# Period: 1
# Date created: 19/11/15
# Date last modified: 20/01/08
# Name: Mingyuan Lin
# Description: prints out a map for the place where you are

# Locations and descriptions

# These are the rooms you are going to go throw in the game

# locations = {
#    'Room 1': {
#        'Description': 'is the guest room and the starting room',
#        },
#    'Room 2': {
#        'Description': 'is the master room',
#        },
#    'Room 3': {
#        'Description': 'is the living room',
#        },
#    'Room 4': {
#        'Description': 'is the basement',
#        },
#    }

# print("\nThese are the locations you are going to investe in the house:")
# for room, room_info in locations.items():
#    description = room_info['Description']

#    print(f"\t{room} {description}.")


# defining the layout of the house
# house_map = [
#     ['Guest Room (Start)', 'Living Room'],
#     ['Master Room', 'Living Room'],
#     ['Basement', 'Basement']
# ]


# def print_map():
#     """print out the map in array"""
#     print("This is the layout of the house you are in: ")
#     for map in house_map:
#         print(map)


# adopted code from Ms. Cotcher

class ViewMap:
    def print_house(self):
        """prints a visual map"""
        self.house_printable = """
        |(you are here)|      |--------------|---------------|
        |  Guest Room  |       Hidden stairs |    Basement   |
        |              |      |--------------|               |
        ---------------- Hall |              |---------------|
        |              |      |                              |
        | Master Room  |     stairs       Living Room        |
        |              |      |                              |
        ----------------------|------------------------------|
        """
        print(self.house_printable)
