from hw13.proxy.interfaces.iwrite import Write
from hw13.proxy.interfaces.iread import Read
from hw13.proxy.txt_reader import TxtReader


class ProxyTxtRW(Read, Write):

    def __init__(self, real_reader: Read, real_writer: Write):
        self.__result = ''
        self.__is_actual = None
        self.__real_reader = real_reader
        self.__real_writer = real_writer

    def read(self):
        if self.__is_actual:
            return self.__result
        else:
            self.__result = self.__real_reader.read()
            self.__is_actual = True
            return self.__result

    def write(self, new_text):
        # зайвий раз не записуємо, якщо цей текс там вже є
        if not self.__is_actual:
            return Exception("Cannot write data without first reading from the file.")
        else:
            self.__result = self.__real_writer.write(new_text)
            self.__is_actual = True
            # return new_text


if __name__ == '__main__':
    reader_reader = TxtReader('my_file.txt')
    writer_new = TxtReader('my_file.txt')
    proxy = ProxyTxtRW(reader_reader, writer_new)
    print(proxy.read())  # тут прочитали файл
    print(proxy.read())  # тут вже не читаємо, а забираємо текст файлу
    proxy.write("message")
