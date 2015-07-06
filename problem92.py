"""
A number chain is created by continuously adding the square of the digits
in a number to form a new number until it has been seen before.

For example,

44 -> 32 -> 13-> 10 -> 1 -> 1
85 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89

Therefore any chain that arrives at 1 or 89
will become stuck in an endless loop.
What is most amazing is that EVERY starting number
will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?

"""


def next_number(current_num):
    """
    Return next number in the chain

    Test:
    >>> next_number(1)
    1
    >>> next_number(9999999)
    567
    """
    res = 0
    while current_num > 0:
        temp = current_num % 10
        res += temp * temp
        current_num /= 10
    return res


def end_of_chain(start_num):
    """
    Find the end number if chain with a given start number

    Test:
    >>> end_of_chain(7)
    1
    >>> end_of_chain(89)
    89
    """
    res = 0
    if start_num == 1 or start_num == 89:
        res = start_num
    else:
        res = end_of_chain(next_number(start_num))
    return res


if __name__ == "__main__":
    early_end = dict()
    final_res = 0
    for i in range(1, 568):
        early_end[i] = end_of_chain(i)
    for n in range(1, 10000001):
        end_number = early_end[next_number(n)]
        if end_number == 89:
            final_res += 1
    print final_res
    import doctest
    doctest.testmod()
