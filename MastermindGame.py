

# Enter Code Below ---------------------------------
# HEADER --------------------------
# Name: Jessica Twumasi
# Date: April 1st, 2024
# Description: A Program that prints that plays a simplified version
# of the game 'Mastermind'
# ---------------------------------
import ErrorMessages
error = ErrorMessages

import ValidityChecks
v = ValidityChecks

# import AllCheck
# allcheck = AllCheck

import Pegs
p = Pegs

import Results
results = Results
# ****************************************************************
legal_colors = ['R', 'G', 'B', 'Y', 'W', 'O', 'M', 'V']


def generate_color_sequence():
    import random
    random.seed()
    sequence = random.sample(range(len(legal_colors)), 4)
    return [legal_colors[i] for i in sequence]


colors = generate_color_sequence()

# ****************************************************************

color_list = []
for i in colors:
    color_list.append(i)  # list of each color chosen by generator

allcolor = "".join(colors)  # formats like this >> RVMO, to read as 1 string

# Rules:
# ~ entries are letters only
# ~ entries must be a valid color
# ~ cannot repeat previously made entries
# ~ entries length must be 4 characters
# ~ entries are converted to uppercase

ask_list = []   # list will store the entries we ask the use for

def game(guesses=5, count=1): # main game
    # Ref: color_list for comp generator  ,  ask_list for user entries
    # guesses = 5  # starts with 5 guesses
    # count = 1
    solution = f'The correct sequence was: {allcolor} .'
    while guesses > 0:  # MAIN CONDITION -- based on guesses
        checks = 0
        go = (f'\nGuess {str(count)}: ')
        ask = input(go).upper()  # will print as: Guess {number}: __

        for i in ask:
            ask_list.append(i)  # ex: RYCM -> ['R', 'Y', 'C', 'M']

        if ask == "QUIT":
            results.lose()
            print(solution)
            break

        # do all the validity checks, if good keep going
        # character validity check
        if not v.char_valid(ask):
            error.char_error()
        else:
            checks += 1
        # color validity check
        if not v.color_valid(ask_list):
            error.color_error()
        else:
            checks += 1
        # unique entry validity check
        if not v.unique_entry_valid(ask):
            error.repeat_error()
        else:
            checks += 1
        # length validity check
        if not v.length_valid(ask):
            error.length_error()
        else:
            checks += 1
        print(f'How many check so far....{checks}/4 | Note: If you pass all the checks with 4/4, you get another guess :)')

        if checks == 4:
            guesses -= 1    # guesses will decrement at wrong VALID entries only
            count += 1
            # if it passes all the checks and the guesses count goes down....
            p.peg_place()     # print out string of W, R, OR _ according to user entry vs comp sequence

        # show the list again to help the player
        print("\n~ Possible colors are: R, G, B, Y, W, O, M, V ~")

        ask_list.clear()    # clear list to reuse after every entry

        # Endgame -- compare comp and user entries as 2 strings || allcolor vs ask
        if ask == allcolor:
            results.win()
            print(solution)
            break
        elif guesses == 0 and ask != allcolor:
            results.lose()
            print(solution)
            break

def endgame():
    pass

# END -----------------------------------------------------------------------------------------------------------------

