

# Enter Code Below ----------------------------------------------

legal_colors = ['R', 'G', 'B', 'Y', 'W', 'O', 'M', 'V']
goodcolors = legal_colors

# Check validity of entries (no guesses used up) >>>>>>>>>>>>>>>>>>>>>>
def char_valid(x):  # check if STRING entry is char
    if x.isalpha():
        return True
    else:
        return False


def color_valid(x):  # LIST; check that all user entry indexes can be found in legal_colors
    # check every index in list of entries that the user gives
    # against the list of given colors
    diff = []
    same = []

    # different colors
    for i in x:
        if not i in goodcolors:
            diff.append(i)

    if len(diff) != 0:
        diff.clear()
        return False

    # matching colors
    for ii in x:
        if ii in goodcolors:
            same.append(ii)

    if len(same) == 4:
        same.clear()
        return True


def unique_entry_valid(x):  # checks STRING
    for i in x:
        if x.count(i) == 1:  # the count of a single char should be 1
            return True
        elif x.count(i) > 1: # safety net
            return False
        else:
            return False


def length_valid(x):
    if len(x) == 4:
        return True
    else:
        return False

# <<<<<<<<<<<<<<<<<<<<<<<< Check validity of entries (no guesses used up)







