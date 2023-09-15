# 1 - Відкрити файл test_file.csv, прочитати його, зп співробітників у доларах перевести в гривні на поточну дату
# (курс задається окремою змінною). Результат зберегти новий файл salaries_uah.csv

import os
import csv

currency_rate = 36.5686

with open('test_file.csv', 'r') as f:
    data = f.readlines()


result = []
for text in data:
    new_data = text.rstrip('\n')
    # print(text)

    new_list = []
    split = new_data.split(",")
    # print(split_0)
    for item in split:
        if item.isdigit():
            item_curr = int(item) * currency_rate
            # print(item_curr)
            new_list.append(str(round(item_curr)))
        else:
            new_list.append(item)
    # print(new_list)

    result.append(new_list)
print(result)


with open('salaries_uah.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(result)
