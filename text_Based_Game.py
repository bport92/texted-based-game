"""
Name: Adventure Text Base Game CLUE
Author:Brandon Porter
Date: 04_12_2022
    Synopsis:
        A text based game where you have to find all of the weapons to solve who the murderer is.
"""


def showIntroduction():
    print()
    print("     WELCOME TO THE CLUE GAME! ")
    print("VV  READ THE INSTRUCTIONS BELOW  VV \n")
    print("In each room, you will be told which directions you can go.")
    print("You can move north, south, east, or west by typing")
    print("the direction you choose.")
    print("You will need to gather all the weapons ")
    print("to find out who the murderer is ")
    print("The weapons present themselves in the text,")
    print("to pick them up type ""get"" and the item name")
    print("Type quit or exit to end the program.")


def run():
    # room list
    rooms = {

        'TopFloor': {'name': 'the TopFloor', 'south': 'Ballroom', 'north': 'Hall', 'east': 'Dining Room',
                     'west': 'Ballard Room', 'items': []},

        'Ballroom': {'name': 'the Ballroom', 'north': 'TopFloor', 'east': 'Kitchen', 'items': ['wrench']},

        'Kitchen': {'name': 'the Kitchen', 'west': 'Ballroom', 'items': []},

        'Hall': {'name': 'The Hall', 'south': 'TopFloor', 'east': 'Lounge', 'west': 'Study', 'items': []},

        'Lounge': {'name': 'the Lounge', 'west': 'Hall', 'items': ['candlestick']},

        'Study': {'name': 'the Study', 'east': 'Hall', 'south': 'Library', 'items': ['leadpipe']},

        'Library': {'name': 'the Library', 'north': 'Study', 'items': ['revolver']},

        'Dining Room': {'name': 'the Dining Room', 'west': 'TopFloor', 'items': ['rope']},

        'Ballard Room': {'name': 'the Ballard Room', 'east': 'TopFloor', 'south': 'Conservatory', 'items': []},

        'Conservatory': {'name': 'the Conservatory', 'north': 'Ballard Room', 'items': ['knife']}
    }

    directions = ['north', 'south', 'east', 'west']
    current_room = rooms['TopFloor']
    inventory = []

    while True:
        if current_room['name'] == 'the Kitchen' and len(inventory) == 6:
            print(' Good Job!!! You have discovered it was Col Mustard in the Kitchen!')
            break
        elif current_room['name'] == 'the Kitchen':
            print('You lost! Please play again. ')
            break
        # display current location
        print()
        print('You are in {}.'.format(current_room['name']))
        # display movable objects
        if current_room['items']:
            print('In the room are: {}'.format(', '.join(current_room['items'])))
        # get user input
        command = input('\nWhat do you do? ').strip()
        # movement
        if command in directions:
            if command in current_room:
                current_room = rooms[current_room[command]]
            else:
                # bad movement
                print("You can't go that way.")
        # quit game
        elif command.lower() in ('exit', 'quit'):
            break
        # gather objects
        elif command.lower().split()[0] == 'get':
            item = command.lower().split()[1]
            if item in current_room['items']:
                current_room['items'].remove(item)
                inventory.append(item)
                print("Inventory = ")
                print(inventory)
            else:
                print("I don't see that here.")
        # get rid of objects
        elif command.lower().split()[0] == 'drop':
            item = command.lower().split()[1]
            if item in inventory:
                current_room['items'].append(item)
                inventory.remove(item)
            else:
                print("You aren't carrying that.")
        # bad command
        else:
            print("I don't understand that command.")


if __name__ == '__main__':
    showIntroduction()
    run()
    play_again = input('Would you like to play again? yes or no? ')
    if play_again == 'yes':
        run()
    # game loop
