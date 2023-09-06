# Створіть словник з чотирма назвами мов програмування (ключі) та іменами розробників цих мов (значення).
# Виведіть по черзі для усіх елементів словника повідомлення типу My favorite programming language is Python.
# It was created by Guido van Rossum.. Видаліть, на ваш вибір, одну пару «мова: розробник» із словника.
# Виведіть словник на екран.

dict_lang = {"python": "Guido van Rossum", "java": "James Gosling", "js": "Brendan Eich", "ruby": "Yukihiro Matsumoto"}
for lang, name in dict_lang.items():
    print(f"My favorite programming language is {lang.title()}. It was created by {name.title()}.")

dict_lang.pop("ruby")
print(dict_lang)
