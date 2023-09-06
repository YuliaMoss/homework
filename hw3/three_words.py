# 4. Користувач вводить текст через пробіл. Конвертувати текст у список.
# Вивести останні 3 елементи зі списку, якщо список містить менше 3-х елементів,
# вивести повідомлення про те що кількість елементів менша за 3 і вказати кількість елементів поточного списку
text = input("Enter the text: ")

new_list = text.split()
number_items = len(new_list)

if number_items >= 3:
    print(new_list[-3:])
elif number_items < 3:
    print(f"The number of items of the list is less then 3: {number_items}")
