

# Enter Code Below ------------------------------------------
def intro():
    possible_colors = "\n~ Possible colors are: R, G, B, Y, W, O, M, V ~" \
                      "\n( Red, Green, Blue, Yellow, White, Orange, Magenta, Violet )"
    rules = "\nRules & Regulations:" \
            "\n* Guess the 4 color sequence the computer will generate." \
            "\n* You need not enter the full name, just the letter." \
            "\n* Enter your guess as 4 letters with no spaces. Do not repeat colors." \
            "\n* You will have five (5) guesses to find the answer." \
            "\n\n* White Peg (W) means correct color(s) are in the wrong place" \
            "\n* Red Peg (R) means correct color(s) are in the right place" \
            "\n* Underscore (_) means color(s) not in computer sequence at all" \
            "\n\n* Enter 'QUIT' to exit the game at any time.\n"
    print(f'Welcome to Mastermind! \n{rules} \n{possible_colors}')
