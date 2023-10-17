from hw13.proxy.interfaces.iwrite import Write
from hw13.proxy.interfaces.iread import Read


class TxtReader(Read, Write):

    def __init__(self, file_path: str):
        self.__file_path = file_path

    def read(self):
        with open(self.__file_path, 'r') as file:
            return file.read()

    def write(self, new_text):
        with open(self.__file_path, 'w') as file:
            return file.write(new_text)
