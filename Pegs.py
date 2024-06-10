

# Enter Code Below ------------------------------------------
import MastermindGame
game = MastermindGame

# Pegs ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Conditionals
# 2 correct colors are in the wrong place {WHITE}
# 1 correct color is in the right place {RED}
# color not in comp sequence at all {UNDERSCORE}
# W, R, U == white, red, underscore

def peg_place():  # where we put the pegs
    # if it passes all the checks and the guesses count goes down....
    r = chr(164)
    w = "?"
    u = "_"
    peg_list = []
    for i in game.ask_list:
        peg_list.append(i)  # put all ask_list entries into peg_list

    # print(f'Check for peg_list ... {peg_list}')  # tracing

    # while you did not win on the 1st try...
    while game.ask_list != game.color_list:
        # underscore
        for i in range(len(peg_list)):
            if game.ask_list[i] not in game.color_list:
                peg_list[i] = u

        # white peg
        for i in range(len(peg_list)):
            if game.ask_list[i] != game.color_list[i] and peg_list[i] != u:
                peg_list[i] = w

        # red peg
        for i in range(len(peg_list)):
            if game.ask_list[i] == game.color_list[i]:
                peg_list[i] = r

        # convert to string then break...
        peg_string = " ".join(peg_list)
        print(peg_string)
        break
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Pegs
