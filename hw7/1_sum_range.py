"""1- Напишіть функцію sum_range(start, end), яка підсумовує всі цілі числа від значення start до величини end включно.
Якщо користувач задасть перше число більше, ніж друге, просто поміняйте їх місцями."""


def sum_range(start, end):
    if start < end:
        result = sum(range(start, end + 1))

    elif start > end:
        result = sum(range(end, start + 1))

    return result


if __name__ == '__main__':
    print(sum_range(2, 5))
    print(sum_range(5, 2))
