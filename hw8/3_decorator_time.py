"""3- Створіть декоратор, який повертає результат функції, а також час за який вона виконана.
Підсказка (для фіксації часу імпортуйте модуль time:  import time)"""

import time


def decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        result = end_time - start_time
        print(result)

    return wrapper


@decorator
def square_quad(some_num):
    result = None
    for num in range(some_num):
        result = num * num
    print(result)

    return result


square_quad(100000)
