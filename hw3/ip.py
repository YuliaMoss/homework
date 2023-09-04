# Додати перевірку введеної IP-адреси. Адреса вважається коректно заданою, якщо вона:
#
# - складається з 4 чисел (а не літер чи інших символів)
# - числа розділені точкою
# - кожне число в діапазоні від 0 до 255 Якщо адреса неправильна, виводьте повідомлення: «Неправильна IP-адреса». Повідомлення "Неправильна IP-адреса" має виводитися лише один раз, навіть якщо кілька пунктів вище не виконані.
#
# Обмеження: завдання треба виконувати, використовуючи лише пройдені теми.

ip_address = input("Enter your IP: ")

numbers = ip_address.split(".")

if len(numbers) == 4:
    valid_ip = (numbers[0].isdigit() and 0 <= int(numbers[0]) <= 255 and
                numbers[1].isdigit() and 0 <= int(numbers[1]) <= 255 and
                numbers[2].isdigit() and 0 <= int(numbers[2]) <= 255 and
                numbers[3].isdigit() and 0 <= int(numbers[3]) <= 255)
else:
    valid_ip = False

message = "IP-адреса вірна" if valid_ip else "Неправильна IP-адреса"
print(message)
