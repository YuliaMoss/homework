"""2- Створіть функцію, яка може повертати квадрати парних чисел у діапазоні від 0 до 1000000000 включно.
Рішення має працювати і не фрізити комп’ютер."""


def gen_range(range_num):
    for num in range(range_num + 1):
        # yield num
        if num % 2 == 0:
            result = num * num
        else:
            continue
        # print(result)
        yield result


gen = gen_range(1000000000)

for i in gen:
    print(i)

# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
