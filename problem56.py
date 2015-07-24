#!/usr/bin/python3
"""
A googol (10^100) is a massive number: one followed by one-hundred zeros;
100^100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100,
what is the maximum digital sum?

"""


def power(base, exp):
    """
    Return base^exp
    Test:
    >>> power(2, 10)
    1024
    >>> power(1, 0)
    1
    """
    res = 0
    temp = 0
    if base == 1 or exp == 0:
        res = 1
    elif base == 0:
        res = 0
    else:
        temp = power(base, exp/2)
        if exp % 2 == 0:
            res = temp * temp
        else:
            res = temp * temp * base
    return res


def digit_sum(number):
    """
    Return sum of all digits of a number
    Test:
    >>> digit_sum(1000)
    1
    >>> digit_sum(123456789)
    45
    """
    res = 0
    while number > 0:
        res += number % 10
        number = number/10
    return res


def main():
    max_dsum = 0
    for i in range(1, 100):
        for j in range(1, 100):
            temp = digit_sum(power(i, j))
            if temp > max_dsum:
                max_dsum = temp
    print(max_dsum)


if __name__ == '__main__':
    main()
