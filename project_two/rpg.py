#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""

# global variables to be modified in main() function
# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
rooms = {
    'Attic': {
        'desc': 'It\'s quite dusty up here!',
        'south': 'Upstairs Hall',
        'item': 'key'
    },
    'Children\'s Room': {
        'desc': 'There are toys scattered everywhere, and a suspicious bear in the corner...',
        'west': 'Upstairs Hall',
        'east': 'Children\'s Bathroom'
    },
    'Children\'s Bathroom': {
        'desc': 'Shiny and decorated with shark....EVERYTHING!',
        'west': 'Children\'s Room',
        'item': 'coordinates'
    },
    'Den': {
        'desc': 'There\'s a fireplace and large couch. The lazy boy looks comfy, but we have a bigger mission to accomplish.',
        'south': 'Hall',
        'east': 'Secret Room'
    },
    'Dining Room': {
        'desc': 'A grand table with chairs and a china cabinet dominate the room.',
        'west': 'Hall',
        'south': 'Garden',
        'east': 'Laundry Room',
        'north': 'Living Room',
    },
    'Front Lawn':{
        'desc': 'NOT AN EXIT!!!!',
        'east': 'Foyer',
        'item': 'monster'
    },
    'Foyer': {
        'desc': 'Another hallway?! Oh no, this is a foyer.',
        'south': 'Garage',
        'north': 'Upstairs Hall',
        'east': 'Hall',
        'west': 'Front Lawn'
    },    
    'Garden': {
        'desc': 'Lush green plants fill the space, with a trickling fountain dawned with a statue of Dumbo...interesting decor choice.',
        'north': 'Dining Room'
    },
    'Garage': {
        'desc': 'Tools and discarded lawn tools litter the floor. No shiny Corvette here.',
        'north': 'Foyer'
    },
    'Hall': {
        'desc': 'The wind howls slightly from holes in the floor boards...',
        'south': 'Kitchen',
        'east': 'Dining Room',
        'north': 'Den',
        'west': 'Foyer'
    },
    'Kitchen': {
        'desc': 'Granite counters, stainless steel appliances, and a full pantry. A nice place to camp and plot',
        'north': 'Hall',
    },
    'Laundry Room': {
        'desc': 'The washer looks full of clothes that may have been there for a while...Best not to open it.',
        'west': 'Dining Room'
    },
    'Living Room': {
        'desc': 'The furniture is minimal, with DEEP scratches in the flooring.',
        'south': 'Dining Room',
        'item': 'monster'
    },
    'Master Bathroom': {
        'desc': 'A bearclaw tub sits in the center of the room, surrounded by hundreds of candles.',
        'east': 'Master Bedroom'
    },
    'Master Bedroom': {
        'desc': 'A decadent room with odd paintings and a color scheme that reminds you of spring rain.',
        'north': 'Roof',
        'south': 'Patio',
        'west': 'Master Bathroom',
        'east': 'Upstairs Hall'
    },
    'Patio': {
        'desc': 'You see a monster roaming the lawn below. Best not to escape through the front door...',
        'north': 'Master Bedroom',
        'item': 'potion'
    },
    'Roof': {
        'desc': 'What are you doing up HERE?',
        'south': 'Master Bedroom'
    },
    'Secret Room': {
        'desc': 'This is where your mission ends...but do you have the key, potion, and coordinates?',
        'west': 'Den'
    },
    'Upstairs Hall': {
        'desc': 'It\'s fairly quiet up here...You should be safe for now.',
        'north': 'Attic',
        'east': 'Children\'s Room',
        'south': 'Foyer',
        'west': 'Master Bedroom'
    }
}

# start the player in the Hall
currentRoom = 'Hall'

def showInstructions():
    """Show the game instructions when called"""
    # print a main menu and the commands
    print('''
    RPG Game
    ========
    Commands:
      go [direction]
      get [item]
    To win the game, get to the secret room with the key, potion, and coordinates to win! Avoid the monsters or it'll be...hasta la vista!!
    ''')


def showStatus():
    """determine the current status of the player"""
    global rooms
    
    # print the player's current location
    print('---------------------------')
    print('You are in the ' + currentRoom + '. ' + rooms[currentRoom]['desc'])
    # print what the player is carrying
    print('Inventory:', inventory)
    # check if there's an item in the room, if so print it
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")


def main():

    # pull in global variables to use in function
    global currentRoom, inventory, rooms

    showInstructions()

    # breaking this while loop means the game is over
    while True:
        showStatus()

        # the player MUST type something in
        # otherwise input will keep asking
        move = ''
        while move == '':
            move = input('What do you want to do? >')

        # normalizing input:
        # .lower() makes it lower case, .split() turns it to a list
        # therefore, "get golden key" becomes ["get", "golden key"]
        move = move.lower().split(" ", 1)

        # if they type 'go' first
        if move[0] == 'go':
            # check that they are allowed wherever they want to go
            if move[1] in rooms[currentRoom]:
                # set the current room to the new room
                currentRoom = rooms[currentRoom][move[1]]
            # if they aren't allowed to go that way:
            else:
                print('You can\'t go that way!')

        # if they type 'get' first
        if move[0] == 'get':
            # make two checks:
            # 1. if the current room contains an item
            # 2. if the item in the room matches the item the player wishes to get
            if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
                # add the item to their inventory
                inventory.append(move[1])
                # display a helpful message
                print(move[1] + ' got!')
                # delete the item key:value pair from the room's dictionary
                del rooms[currentRoom]['item']
            # if there's no item in the room or the item doesn't match
            else:
                # tell them they can't get it
                print('Can\'t get ' + move[1] + '!')

            # If a player enters a room with a monster
        if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
            print('A monster has got you... GAME OVER!')
            break

            # Define how a player can win
        if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
            print(
                'You escaped the house with the ultra rare key and magic potion... YOU WIN!')
            break


main()
