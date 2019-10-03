import sys
import random

from room import Room
from player import Player
from item import Item, Lightsource

# Declare all the rooms

room = {
    'outside': Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", is_light = False),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers.""", is_light = False),

    'empty': Room("Empty Room", """You walked into an room that seems empty at first glance. To the east is a passage.""")
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['foyer'].w_to = room['empty']
room['overlook'].s_to = room['foyer']
room['empty'].e_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player('Player_One', room['outside'])

# Declare all the items

item = {
    'blade': Item('Blade', 'sharped blade'),
    'sword': Item('Sword', 'shiny sword'),
    'shield': Item('Shield', 'wooden shield'),
    'hammer': Item('Hammer', 'rusty hammer'),
    'staff': Item('Staff', 'magical staff of fire'),
    'lamp': Lightsource('Lamp', 'a source of light')
}

# Place items in rooms randomly

for _ in range(0, 4):
    rand_room = random.choice(list(room.keys()))
    rand_item = random.choice(list(item.keys()))
    room[rand_room].add_item(rand_item)


game_over = False
choices = ['n', 'e', 's', 'w']
actions = ['get', 'take', 'pick', 'drop', 'check']
directions = {'n': 'North', 'e': 'East', 's': 'Sud', 'w': 'West'}


def get_command():
    return input('Command> ').lower().split(' ')


def move_player(room, cmd):
    cmd_to = cmd + '_to'
    if hasattr(room, cmd_to):
        print(f'You move {directions[cmd]}')
        player.set_current_room(getattr(room, cmd_to))
        player.current_room.describe(lamp = 'lamp' in player.inventory)
        if player.current_room.name == 'Treasure Chamber':
            global game_over
            game_over = True
        print('')
    else:
        print('nothing there')


def pick(obj):
    if obj in player.current_room.items:
        player.current_room.remove_item(obj)
        player.pick_item(obj)
        item[obj].on_pick()
    else:
        print(f'There is no {obj} in this room')

def drop(obj):
    if obj in player.inventory:
        player.drop_item(obj)
        player.current_room.add_item(obj)
        item[obj].on_drop()        
    else:
        print(f'There is no {obj} in your inventory')

def get_help():
    print('type n, e, s or w to move or q to quit')

#first description on game start
player.current_room.describe()
room['empty'].add_item('lamp')

while not game_over:
    cmd = get_command()
    # command verb, first input
    cmd_v = cmd[0]
    
    if cmd_v == 'q':
        game_over = True
    elif cmd_v in choices:
        move_player(player.current_room, cmd_v)
    elif cmd_v == 'i' or cmd_v == 'inventory':
        print(f'You carry {player.inventory}')
    elif cmd_v in actions:
        if cmd_v in actions[:3]:
            pick(cmd[1])
        elif cmd_v == 'drop':
            drop(cmd[1])
        elif cmd_v == 'check':
            player.current_room.check()
    else:
        get_help()





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