"""3- Напишіть функцію з такою сигнатурою: def display_box(width: int, height: int, character="*") .
Ця функція намалює простий прямокутник заданої висоти та ширини, використовуючи character для друку ліній.
Наприклад, display_box(5, 4, 'x') має вивести наступне:
xxxxx
x   x
x   x
xxxxx"""


def display_box(width: int, high: int, character="*"):
    result = []
    width_print = width * character
    result.append(width_print)

    if width >= 2:
        high_print = character + ' ' * (width - 2) + character
        for h in range(high - 2):
            result.append(high_print)
    else:
        high_print = character * (high - 2)
        for h in high_print:
            result.append(h)

    if high >= 2:
        result.append(width_print)

    return "\n".join(result)


if __name__ == '__main__':
    print(display_box(5, 4, "x"))
    print(display_box(1, 1, "x"))
    print(display_box(2, 2, "x"))
    print(display_box(4, 1, "x"))
    print(display_box(1, 4, "x"))
