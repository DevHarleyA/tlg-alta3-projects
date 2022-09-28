#!/usr/bin/env python3

"""Welcome to the National Park Questionnaire! 
Looking for a new national park trip but can't seem to choose from all the options? Take this questionnaire to determine where your next national park vacation will be!

Project One submission by A.Harley for TLG-ALTA3"""

def main():

    # create a list that will contain all of the possible answers
    # list version
    parks = ["Yosemite National Park", "Zion National Park", "Wind Cave National Park", "Virgin Islands National Park", "Acadia National Park"]

    # dictionary version
    parks_dict = {
        'Yosemite National Park': {
            'seasons': ['winter', 'spring'],
            'bears': True,
            'coast': 'west',
            'terrain': 'mountains',
            'woods': True
        },
        'Zion National Park': {
            'seasons': ['spring', 'fall'],
            'bears': False,
            'coast': 'west',
            'terrain': 'canyons',
            'woods': False
        },
        'Wind Cave National Park': {
            'seasons': ['summer'],
            'bears': False,
            'coast': 'none',
            'terrain': 'hills',
            'woods': True
        },
        'Virgin Islands National Park': {
            'seasons': ['spring'],
            'bears': False,
            'coast': 'east',
            'terrain': 'hills',
            'woods': True
        },
        'Acadia National Park': {
            'seasons': ['fall'],
            'bears': True,
            'coast': 'east',
            'terrain': 'mountains'
        }
        }

    # while loop around inputs 
    round = 0

    while round < 5:

        # Q1: What is your favorite season? (winter, summer, spring, autumn)
        season = input("What is your favorite season?:\n(a) spring\n(b) summer\n(c) fall\n(d) winter\nYour answer: ")
        
        # if the user answers spring, remove Acadia and Wind Cave from the list
        if season == 'a':
            parks.remove('Wind Cave National Park')
            parks.remove('Acadia National Park')
            # increment round counter to continue to next question
            round += 1

        # if the user answers summer, return Wind Cave (only park recommended visit in the summer)
        elif season == 'b':
            print(f"You should visit {parks[2]}")
            break
        
        # if the user answers fall, remove Virgin Islands, Wind Cave, and Yosemite
        elif season == 'c':
            parks.remove('Virgin Islands National Park')
            parks.remove('Wind Cave National Park')
            parks.remove('Yosemite National Park')
            # increment round counter to continue to next question
            round += 1

        # if the user answers winter, return Yosemite National Park
        elif season == 'd':
            print(f"You should visit {parks[0]}")
            break

        else:
            print("That's not an acceptable answer. Please answer again.")
 
    # Q2: Are you afraid of Bears? (Y/N)
        if round == 1:

            bears = input("Are you afraid of bears?\n(a) Hell Yeah!\n(b) Nah, bring it on!\nYour answer:")

        if bears == 'a':
            if parks.count("Yosemite National Park") == 1:
                parks.remove('Yosemite National Park')
            if parks.count('Acadia National Park') == 1:
                parks.remove('Acadia National Park')
            # increment round counter to continue to next question
            round += 1

        elif bears == 'b':
            # increment round counter to continue to next question
            round += 1

        elif parks.len() == 1:
            print(f"You should visit {parks[0]}")
            break

        else:
            print("That's not an acceptable answer. Please answer again.")
    # Q3: Do you prefer the East Coast or the West Coast?

    # Q4: Do you want to see mountains, hills, or canyons?

    # Q5: Do you like plaid? (Lumberjack Reference, remove non-woodsy parks if no (false))

    # conditionals for variables






main()