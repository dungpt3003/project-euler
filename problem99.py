"""
Comparing two numbers written in index form like 2^11 and 3^7 
is not difficult, as any calculator would confirm that 2^11 = 2048 < 3^7 = 2187.

However, confirming that 632382^518061 > 519432^525806 would be much more difficult, 
as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), 
a 22K text file containing one thousand lines with a base/exponent pair on each line, 
determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above.
"""
import math
EXP_LIST = list()

def main():
    global EXP_LIST
    with open('data/p099_base_exp.txt') as file1:
        for line in file1:
            num = int(line.split(',')[0].rstrip())
            exp = int(line.split(',')[1].rstrip())
            EXP_LIST.append((num, exp))
    print find_max_value(EXP_LIST)


def value_of_pair(n, e):
    """
    Return natural logarithm of n^e

    Test:
    >>> value_of_pair(1, 123456)
    0.0
    >>> value_of_pair(632382, 518061)
    6919869.733217769
    """
    return e * math.log(n)


def find_max_value(lst):
    """
    Return position of maximum value in a list of (base, exponent)

    Test:
    >>> find_max_value([(1,2), (3,3), (2,5)])
    3
    """
    res_value = 0
    res_pair = (0, 0)
    for pair in lst:
        temp = value_of_pair(pair[0], pair[1])
        if temp > res_value:
            res_value = temp
            res_pair = pair
    return lst.index(res_pair) + 1


if __name__ == '__main__':
    main()
    import doctest
    doctest.testmod()