"""
By counting carefully it can be seen that a rectangular grid measuring
3 by 2 contains eighteen rectangles.
Although there exists no rectangular grid that contains exactly
two million rectangles, find the area of the grid with the nearest solution.
"""
import math


def sum_from_one(number):
    """
    Return sum of numbers from 1 to given number.
    """
    return number * (number + 1) / 2


def number_of_rec(length, width):
    """
    Count number of rectangles that grid of length * width contains
    """
    res = sum_from_one(length) * sum_from_one(width)
    return res


def main():
    """
    Find the area of the grid with the nearest solution.
    """
    nearest = 2000000
    res_area = 1
    for i in range(1, 100):
        for j in range(1, 100):
            temp = math.fabs(number_of_rec(i, j) - 2000000)
            if temp < nearest:
                nearest = temp
                res_area = i * j
    print(res_area)


if __name__ == '__main__':
    main()
