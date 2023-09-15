# 2- Написати програму, яка просканує кореневу папку вашого проєкту, збереже у файл files_size.txt назви та розмір
# файлів, і надрукує назву найбільшого файлу та його розмір.
import os

file_size = []
for root, dirs, files in os.walk('./..'):
    for file_name in files:
        file_names = file_name
        size = os.path.getsize(os.path.join(root, file_name))
        file_size.append(size)

        all_info = file_names + ", " + str(size) + "\n"

    with open('files_size.txt', 'a') as file:
        file.write(all_info)

max_size = max(file_size)
print(f"The maximum file size: {max_size} bytes")
