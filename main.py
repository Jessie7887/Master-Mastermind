

# Enter Code Below --------------------------------------------------
import MastermindGame
import RR



def order():
    mastermind = MastermindGame

    mastermind.generate_color_sequence() # get colors
    RR.intro()  # rules & regs
    mastermind.game()   # play game

# idea for strikethrough text....
# def strike(text):
#     result = ''
#     for c in text:
#         result = (f'{result}{c}\u0336')
#         return result


# Run the program.
if __name__ == '__main__':
    order()


