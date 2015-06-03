"""
Each new term in the Fibonacci sequence is generated 
by adding the previous two terms. 

By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence 
whose values do not exceed four million, find the sum 
of the even-valued terms.
"""


def create_fibonacci(n):
    """
    Create fibonacci sequence whose values do not exceed n

    Test:
    >>> create_fibonacci(100)
    [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    """
    fibo = [1,2]
    while (fibo[-1] + fibo[-2] <= n):
	    fibo.append(fibo[-1] + fibo[-2])
    return fibo


def sum_of_even(lst):
    """
    Return sum of all even elements in a list

    Test:
    >>> sum_of_even([1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
    44
    """
    res = 0
    for i in lst:
	    if (i % 2 == 0):
		    res = res + i
    return res


def main():
    print sum_of_even(create_fibonacci(4000000))


if __name__ == '__main__':
    main()
    import doctest
    doctest.testmod()