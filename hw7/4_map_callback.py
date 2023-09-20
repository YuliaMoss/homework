"""4- написати власну функцію map, використовуючи callback"""


# print(list(map(lambda x: x**x, [1, 2, 3, 4, 5])))

def my_map(funct, sequence):
    new_list = []
    for x in sequence:
        result = funct(x)
        new_list.append(result)

    return new_list


if __name__ == '__main__':
    print(my_map(lambda x: x ** x, [1, 2, 3, 4, 5]))
    print(my_map(lambda x: x - 2, [3, 5, 10]))
