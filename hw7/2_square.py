"""2- Напишіть функцію square, яка приймає 1 аргумент, сторону квадрата, і повертає 3 значення :
периметр квадрата, площа квадрата та діагональ квадрата. Надрукуйте їх"""


def square(num):
    perimeter_quad = num + num
    square_quad = num * num
    diagonal_quad = square_quad * square_quad
    return perimeter_quad, square_quad, diagonal_quad


if __name__ == '__main__':
    print(square(2))
    print(square(5))
