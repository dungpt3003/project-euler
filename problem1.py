"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def sum_mutiples(n):
    """
    Return sum of all the multiples of 3 or 5 below n.

    Test:
    >>> sum_mutiples(10)
    23
    """
    res = 0
    for i in range(0,n):
	    if (i % 3 == 0) or (i % 5 == 0):
		    res = res + i
    return res


def main():
    print sum_mutiples(1000)


if __name__ == '__main__':
    main()
    import doctest
    doctest.testmod()