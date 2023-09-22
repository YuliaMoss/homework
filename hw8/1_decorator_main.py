"""1- Створіть декоратор, який виводить в консоль назву викликаної функції.
Наприклад, створіть пару функцій для арифметичних операцій підсумовування та множення.
Під час виклику цих функцій має бути повернутий результат операції,
а ім’я викликаної функції має відображатися на консолі разом із результатом.
Маленька підказка (__name__)"""


def decorator(func):
    def wrapper(a, b):
        print(func.__name__)
        func(a, b)
        print("")

    return wrapper


@decorator
def sum_num(a, b):
    result = a + b
    print(result)


@decorator
def mult_num(a, b):
    result = a * b
    print(result)


sum_num(4, 5)
mult_num(4, 5)
