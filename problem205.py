"""
Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.
Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.

Peter and Colin roll their dice and compare totals: the highest total wins. 
The result is a draw if the totals are equal.

What is the probability that Pyramidal Pete beats Cubic Colin? 
yGive your answer rounded to seven decimal places in the form 0.abcdefg

"""
PYRAMIDAL = dict()
CUBE = dict()
PYR_LIST = [0] * 10
CUB_LIST = [0] * 7


def init():
    global PYRAMIDAL
    global CUBE
    for i in range (6, 37):
        PYRAMIDAL[i] = 0
        CUBE[i] = 0


def sum_of_list(lst):
    """
    Return sum of all elements in a list

    Test:
    >>> sum_of_list([1, 2, 1, 3, 4])
    11
    """
    res = 0
    for number in lst:
        res += number
    return res


def roll_the_pyramidal(n, k):
    """
    Roll the pyramidal to try all possible outcome.
    Output a dictionary where dict[k] is the number of outcomes 
    that have totals = k 
    """
    global PYRAMIDAL        
    global PYR_LIST
    PYR_LIST[n] = k
    if n == 9:
        temp = sum_of_list(PYR_LIST)
        PYRAMIDAL[temp] += 1
        return
    else:
        for i in range(1, 5):
            roll_the_pyramidal(n + 1, i)


def roll_the_cube(n, k):
    """
    Roll the cube to try all possible outcome.
    Output a dictionary where dict[k] is the number of outcomes 
    that have totals = k
    """
    global CUBE
    global CUB_LIST
    CUB_LIST[n] = k
    if n == 6:
        temp = sum_of_list(CUB_LIST)
        CUBE[temp] += 1
        return
    else:
        for i in range(1, 7):
            roll_the_cube(n + 1, i)


def pyramidal_win(pyr, cub):
    """
    Count number of outcomes that Pyramidal win
    """
    res = 0
    for key1 in pyr:
        for key2 in cub:
            if key2 < key1:
                res += pyr[key1] * cub[key2]
    return res


def main():
    init()
    roll_the_pyramidal(0, 0)
    roll_the_cube(0,0)


if __name__ == '__main__':
    main()
    import doctest
    doctest.testmod()
    total_outcome = (4 ** 9) * (6 ** 6)
    total_pyrwin = pyramidal_win(PYRAMIDAL, CUBE)
    print total_pyrwin / float(total_outcome)