# У вас є список змінних у форматі CamelCase ["FirstItem", "FriendsList", "MyTuple"] ,
# перетворити його у список змінних для Пайтона snace_case, "friends_list", "my_tuple"]

camel_case_list = ["FirstItem", "FriendsList", "MyTuple"]
snake_case_list = []


for word in camel_case_list:
    # print(word)
    new_list = []
    for letter in word:
        if letter.isupper():
            if len(new_list) > 0:
                new_list.append('_')
            new_list.append(letter.lower())
            # print(new_list)
        else:
            new_list.append(letter)
    # print(new_list)

    snake_case_list.append(''.join(new_list))

print(snake_case_list)


