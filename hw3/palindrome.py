# 1. Користувач вводить слово, якщо це слово є поліндромом, вивести '+', інакше '-'
word = str(input("Enter the word: "))

result = None

reverse_word = word[::-1]
if word == reverse_word:
    result = "+"
else:
    result = "-"

print(result)
