# task 1

# Написати програму, яка вміє переводити температуру з C в Фаренгейти і Кельвіни Наприклад:
# дана температура в Цельсіях 25 С

# Фаренгейт: 45.9F - вважається за формулою C * 9/5 + 32

# Кельвіни: 298.16K - вважається за формулою C + 273.15

# Користувач вводить температуру в градусах Цельсіях, програма выводить температуру в Фаренгейтах та Кельвінах

celsius = int(input("Enter the temperature in degrees Celsius: "))
fahrenheit = celsius * (9 / 5) + 32
kelvin = celsius + 273.15
print("The temperature in Fahrenheit: ", fahrenheit)
print("The temperature in Kelvin: ", kelvin)

# task 2
2
# Змішано V1 літрів води з температурою T1 та V2 літрів з температурою T2.
# Написати програму, яка порахує об'єм і температуру суміші, що вийшла.
# Обчислюється за формулою (v1 * t1 + v2 * t2) / (v1 + v2)

# Всі параметри виводяться в консолі, вивести обʼєм та температуру

v1 = int(input("Enter the volume of the first part of water: "))
t1 = int(input("Enter the temperature of the first part of water: "))
v2 = int(input("Enter the volume of the second part of water: "))
t2 = int(input("Enter the temperature of the second part of water: "))

volume = (v1 + v2)
temperature = (v1 * t1 + v2 * t2) / volume

print("The volume of the mix: ", volume)
print("The temperature of the mix: ", temperature)


# task 3

# Написать калькулятор с основными операциями(+, -, *, /)

# Користувач вводить два числа та арифметичну операцію

# Також можна додати перевірку для всіх задач з негативним сценарієм

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
operation = input("Enter the math operation you would like to complete (+, -, *, /): ")

if operation == '+':
    print("Result: ", number1 + number2)
elif operation == '-':
    print("Result: ", number1 - number2)
elif operation == '*':
    print("Result: ", number1 * number2)
elif operation == '/':
    if number2 != 0:
        print("Result: ", number1 / number2)
    else:
        print("Cannot divide by zero")
else:
    print("Incorrect operation. Please select from the list: +, -, *, /")


