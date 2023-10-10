from hw12.build_a_train_train.basewagon import BaseWagon


class Train(BaseWagon):

    def __setitem__(self, key, value):
        self.entities[key].add(value)

    def __str__(self):
        new_list = []
        for number, _ in enumerate(self.entities, start=1):
            new_list.append(f"[{number}]")

        message = "-".join(new_list)
        return f"<=[HEAD]-{message}-[...]"
