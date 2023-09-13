# Напишіть інтерактивний калькулятор. Передбачається, що користувач вводить формулу, що складається з числа, оператора
# (як мінімум * і /) та іншого числа, розділених пробілом (наприклад, 2 * 5).
# - Якщо вхідні дані не складаються з трьох елементів, генеруйте та спіймайте власний ексепшн FormulaError.
# - Якщо другий елемент не є «*» або «/», генеруйте та спіймайте власний ексепшн WrongOperatorError
# - Якщо введені числа не можуть бути float спіймайте ValueError
# - Також ловіть помилку при діленні на 0
# - В кожній спійманій помилці друкуйте пояснення, що пішло не так
# - За допомогою циклів (while + counter) або (for + in range) надайте три спроби скористуватись калькулятором,
# якщо введені не вірні дані
# - Використати всі блоки try, except, else, finally. В finally можна надрукувати за скільки спроб виконавлась формула
# - Результат виконання формули - float число з двома знаками після крапки

class FormulaError(Exception):
    pass


class WrongOperatorError(Exception):
    pass


count = 0
while count < 3:

    try:
        input_formula = input("Enter the formula: ")
        split_result = input_formula.split(" ")

        if len(split_result) != 3:
            raise FormulaError("The input date include the wrong formula ")  # FormulaError

        else:
            if split_result[1] not in "/*":
                raise WrongOperatorError("You entered wrong operator")  # WrongOperatorError()
            num1 = int(split_result[0])
            num2 = int(split_result[2])
            operator = split_result[1]

    except ValueError:
        # print(error)
        print("You may entered not an integer")

    except FormulaError as error:
        print(error)
        print("Enter the formula according to the example (2 * 5)")

    except WrongOperatorError as error:
        print(error)
        print("Please select from the list: *, /")

    else:
        try:
            if operator == "/":
                result = num1 / num2

            elif operator == "*":
                result = num1 * num2

        except ZeroDivisionError:
            print("Cannot divide by zero")

        else:
            print(f"Your result: {round(result, 2)}")

    finally:
        print(f"You did {count + 1} attempts")
    count += 1
