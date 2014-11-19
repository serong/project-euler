# -*- coding: utf-8 -*-
"""
    Problem 011 - Largest Product in a Grid
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :description:
    In the 20×20 grid below, four numbers along a diagonal
    line have been marked in red.

    08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
    49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
    81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
    52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
    22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
    24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
    32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
    67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
    24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
    21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
    78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
    16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
    86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
    19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
    04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
    88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
    04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
    20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
    20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
    01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

    The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

    What is the greatest product of four adjacent numbers in the
    same direction (up, down, left, right, or diagonally) in the
    20×20 grid?

    :url:
    https://projecteuler.net/problem=11

    :answer: 70600674
    :time: 0.01s

    :author:
    :updated: 2014-11-19
"""
from time import time
t = time()

# Some preparations... turning the string into a matrix etc.

numbers = """
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
"""

# removing the trailing new-line-breaks.
numbers = numbers[1:-1]

# rows
numbers = numbers.split("\n")

temp = []
# columns
for line in numbers:
    temp.append(line.split(" "))

numbers = temp

# Checking to see if the structure is okay.
print "0\t",
for x in range(20):
    if x < 10:
        print "0" + str(x),
    else:
        print x,
print "\n"

for row in numbers:
    print numbers.index(row), "\t",
    for num in row:
        print num,
    print "\n"

# =========================================================================


def neighbour_right(location, i):
    """ i neighbours to the right.

        :var:location is a tuple of (row, col)
        coordinates.

        >>> neighbour_right((15,0), 4)
        [88, 36, 68, 87]

        >>> neighbour_right((17, 9), 4)
        [62, 99, 69, 82]

        >>> neighbour_right((0, 17), 4)

    """

    row = location[0]
    col = location[1]
    number = numbers[row][col]

    # Location check.
    if col > (20-i):
        return None
    else:
        # Return a list, including the number itself.
        result = [int(number)]

        for n in range(1, i):
            n_row = row
            n_col = col + n
            temp = numbers[n_row][n_col]
            result.append(int(temp))

        return result


def neighbour_down(location, i):
    """ i neighbours to the right.

        :var:location is a tuple of (row, col)
        coordinates.

        >>> neighbour_down((15, 0), 4)
        [88, 4, 20, 20]

        >>> neighbour_down((17, 19), 4)

    """

    row = location[0]
    col = location[1]
    number = numbers[row][col]

    # Location check.
    if row > 20-i:
        return None
    else:
        # Return a list, including the number itself.
        result = [int(number)]

        for n in range(1, i):
            n_row = row + n
            n_col = col
            temp = numbers[n_row][n_col]
            result.append(int(temp))

        return result


def neighbour_down_left(location, i):
    """ i neighbours to the right.

        :var:location is a tuple of (row, col)
        coordinates.

        >>> neighbour_down_left((15, 0), 4)

        >>> neighbour_down_left((17, 3), 4)

        >>> neighbour_down_left((16, 3), 4)
        [73, 36, 73, 1]
    """

    row = location[0]
    col = location[1]
    number = numbers[row][col]

    # Location check.
    if row > (20-i) or col < (i-1):
        return None
    else:
        # Return a list, including the number itself.
        result = [int(number)]

        for n in range(1, i):
            n_row = row + n
            n_col = col - n
            temp = numbers[n_row][n_col]
            result.append(int(temp))

        return result


def neighbour_down_right(location, i):
    """ i neighbours to the right.

        :var:location is a tuple of (row, col)
        coordinates.

        >>> neighbour_down_right((15, 0), 4)
        [88, 42, 36, 29]

        >>> neighbour_down_right((17, 0), 4)

        >>> neighbour_down_right((17, 0), 3)
        [20, 73, 54]
    """

    row = location[0]
    col = location[1]
    number = numbers[row][col]

    # Location check.
    if col > (20-i) or row > (20-i):
        return None
    else:
        # Return a list, including the number itself.
        result = [int(number)]

        for n in range(1, i):
            n_row = row + n
            n_col = col + n
            temp = numbers[n_row][n_col]
            result.append(int(temp))

        return result


# While I ended up writing both neighbour_down and neighbour_left,
# you really need only one of them.


def calculate(alist):
    """ Multiply the elements of the list.

        >>> calculate([10,1,2,3])
        60

        >>> calculate([1,2,3,4])
        24
    """

    result = 1
    for number in alist:
        result = result * number

    return result


def largest_product(n):
    """ Return the largest product.
    """

    largest = 1

    for row in range(20):
        for col in range(20):

            number_list = [
                neighbour_right((row, col), n),
                neighbour_down((row, col), n),
                neighbour_down_left((row, col), n),
                neighbour_down_right((row, col), n)
            ]

            products = []
            for element in number_list:
                if element is not None:
                    products.append(calculate(element))

            if len(products) != 0 and max(products) > largest:
                largest = max(products)
                print "Current largest: ", largest

    print largest


print largest_product(4)
print "Finished in: ", time() - t


if __name__ == "__main__":
    import doctest
    doctest.testmod()
