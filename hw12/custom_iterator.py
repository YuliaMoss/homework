class SequenceIterator:
    def __init__(self, sequence, start_index, stop_index):
        self.sequence = sequence
        self.start_index = start_index
        self.stop_index = stop_index
        self.index = start_index

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.sequence):
            raise StopIteration
        elif self.index < self.stop_index:
            result = self.sequence[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration


if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5]
    my_iter = SequenceIterator(my_list, 1, 6)

    for i in my_iter:
        print(i)
