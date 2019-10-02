import sys
import random

from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player('Player_One', 'outside')

# Declare all the items

item = {
    'blade': Item('Blade', 'sharped blade'),
    'sword': Item('Sword', 'shiny sword'),
    'shield': Item('Shield', 'wooden shield'),
    'hammer': Item('Hammer', 'rusty hammer'),
    'staff': Item('Staff', 'magical staff of ice'),
}

# Place items in rooms randomly

# all_rooms = []
# all_items = []

# for k, v in room.items():
#     all_rooms.append(k)
# for k, v in item.items():
#     all_items.append(k)

# for _ in range(0, 4):
#     r0 = random.randint(1, len(room))
#     r1 = random.randint(1, len(item))
#     # room[all_rooms[r0]].items.append(all_items[r1])
#     # getattr(room[all_rooms[r0]], 'items').append(all_items[r1])
#     print(getattr(room[all_rooms[r0]], 'items'))
#     # print(all_items[r1])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:
    print(f'You are at {player.current_room}')
    print(room[player.current_room].description)
    print(f'Items in this room : {room[player.current_room].items}')
    choices = ['n', 'e', 's', 'w']
    actions = ['get', 'take', 'drop']
    x = input('move to ')
    x = x.split(' ')
    # print(x)

    if x[0] == 'q':
        sys.exit()
    elif x[0] in choices:
        x_to = x[0]+'_to'
        if not hasattr(room[player.current_room], x_to):
            print('nothing there')
        else:
            print('You move North')
            for k, v in room.items():
                if v == getattr(room[player.current_room], x_to):
                    player.set_current_room(k)
                    break
    elif x[0] == 'i' or x[0] == 'inventory':
        print(f'You carry {player.inventory}')
    elif x[0] in actions:
        if x[0] == 'get' or x[0] == 'take':
            if x[1] in room[player.current_room].items:
                room[player.current_room].items.remove(x[1])
                player.inventory.append(x[1])
                item[x[1]].on_take()
            else:
                print(f'There is no {x[1]} in this room')
        elif x[0] == 'drop':
            if x[1] in player.inventory:
                player.inventory.remove(x[1])
                room[player.current_room].items.append(x[1])
                item[x[1]].on_drop()
            else:
                print(f'There is no {x[1]} in your inventory')            
    else:
        print('type n, e, s or w to move or q to quit')

    print('\n')