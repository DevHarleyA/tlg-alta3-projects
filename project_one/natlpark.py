#!/usr/bin/env python3

"""Welcome to the National Park Questionnaire! 
Looking for a new national park trip but can't seem to choose from all the options? Take this questionnaire to determine where your next national park vacation will be!

Project One submission by A.Harley for TLG-ALTA3"""

def main():
    """This is the main function that will run when the script is executed. """

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

    # responses from the survey will be stored in this empty list
    responses = []

    # Q1: What is your favorite season? (winter, summer, spring, fall)
    while True:
        season = input("What is your favorite season?:\n(a) spring\n(b) summer\n(c) fall\n(d) winter\nYour answer: ").lower()
        
        # if the user answers spring, add spring to responses list and move to next question
        if season == 'a':
            responses.append('spring')
            break

        # if the user answers summer, add summer to responses list and move to next question
        elif season == 'b':
            responses.append('summer')
            break
        
        # if the user answers fall, add fall to responses list and move to next question
        elif season == 'c':
            responses.append('fall')
            break

        # if the user answers winter, add winter to responses list and move to next question
        elif season == 'd':
            responses.append('winter')
            break
        
        # if the user does not enter a letter between a-d, prompt the user again.
        else:
            print("That's not an acceptable answer. Please answer again with either 'a', 'b', 'c', or 'd'.")
 
    # Q2: Are you afraid of Bears? (Y/N)
    while True:     
        bears = input("\nAre you afraid of bears?\n(a) Hell Yeah!\n(b) Nah, bring it on!\nYour answer:").lower()

        # if the user asnewers yes, add no bears to responses list and move to next question
        if bears == 'a':
            responses.append('no bears')
            break

        # if the user asnewers no, add bears okay to responses list and move to next question
        elif bears == 'b':
            responses.append('bears okay')
            break

        # if the user does not enter a or b, prompt the user again
        else:
            print("That's not an acceptable answer. Please answer again with either 'a' or 'b'.\n")

    # Q3: Do you prefer the East Coast or the West Coast?
    while True:
        coast = input("\nDo you prefer the west coast or east coast?\n(a) East\n(b) West\nYour answer:").lower()

        # if the answer is a, add east to responses and move to next question
        if coast == 'a':
            responses.append('east')
            break

        # if the answer is b, add east to responses and move to next question
        elif coast == 'b':
            responses.append('west')
            break
        
        # if the user does not enter a or b, prompt the user again.
        else:
            print("That's not an acceptable answer. Please answer again with 'a' or 'b'.\n")
    
    # Q4: Do you want to see mountains, hills, or canyons?
    while True:
        terrain = input("\nWhat do you want to see?\n(a) mountains\n(b) hills\n(c) canyons\nYour answer:").lower()

        # if the user enters a, add mountains to responses list and move to next question
        if terrain == 'a':
            responses.append('mountains')
            break

        # if the user enters b, add hills to responses list and move to next question
        elif terrain == 'b':
            responses.append('hills')
            break

        # if the user enters c, add canyons to responses list and move to next question
        elif terrain == 'c':
            responses.append('canyons')
            break

        # if the user does not enter a letter between a, b, or c, prompt the user again.
        else:
            print("That's not an acceptable answer. Please answer again with 'a', 'b', or 'c'.\n")

    # Q5: Do you like plaid? (Lumberjack Reference)
    while True:
        plaid = input("\nDo you like plaid?\n(a) yes\n(b) no\nYour answer:").lower()

        # if user enters a, then add plaid_yes to responses list and move to next question
        if plaid == 'a':
            responses.append('plaid_yes')
            break

        # if user enters b, then add plaid_no to responses list and move to next question
        elif plaid == 'b':
            responses.append('plaid_no')
            break

        # if the user does not enter a or b, prompt the user again.
        else:
            print("That's not an acceptable answer. Please answer again with 'a', 'b'.\n")
    
    # used line to confirm responses during testing
    # print(f"Your responses were: {responses}")

    # conditionals for variables
    for answer in responses:
        # if the answer is fall, loop through answers to determine coast selection
        if answer == 'fall':
            for answer in responses:
                # if answer is west, respond Zion
                if answer == 'west':
                    return print(f'You should visit {parks[1]}')
                # else return Acadia
                else:
                    return print(f'You should visit {parks[4]}')
        # if answer is winter, return Yosemite
        elif answer == 'winter':
            return print (f'You should visit {parks[0]}!')
        # if answer is summer, return Wind
        elif answer == 'summer':
            return print(f'You should viist {parks[2]}!')
        # if answer is spring, loop through answers again
        elif answer == 'spring':
            for answer in responses:
                # if answer is east, return Virgin Islands
                if answer == 'east':
                    return print(f'You should visit {parks[3]}')
                # if answer is canyons, return Zion
                elif answer == 'canyons':
                    return print(f'You should visit {parks[1]}')
                # else, return Yosemite
                else:
                    return (f'You should visit {parks[0]}!')
        # if something goes wrong, and ALL ELSE FAILS, return a blip.
        else:
            print('Something intriguing happened...maybe you should take the survey again?')



# run the main function containing code
main()