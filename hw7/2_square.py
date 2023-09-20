"""2- Напишіть функцію square, яка приймає 1 аргумент, сторону квадрата, і повертає 3 значення :
периметр квадрата, площа квадрата та діагональ квадрата. Надрукуйте їх"""

import math


def square(side_length):
    perimeter_quad = side_length + side_length
    square_quad = side_length * side_length
    diagonal_quad = side_length * math.sqrt(2)
    return perimeter_quad, square_quad, diagonal_quad


if __name__ == '__main__':
    print(square(2))
    print(square(5))
