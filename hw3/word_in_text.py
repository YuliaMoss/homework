# 2. Користувач вводить текст і слово, яке потрібно знайти, якщо це слово є в тексті, вивести 'YES', інакше 'NO'
text = str(input("Enter the text: "))
word = str(input("Enter the word: "))

value = None

if word in text:
    value = "YES"
else:
    value = "NO"

print(value)
