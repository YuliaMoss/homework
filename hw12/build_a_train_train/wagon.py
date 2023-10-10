from hw12.build_a_train_train.basewagon import BaseWagon


class Wagon(BaseWagon):

    def add(self, passenger):
        if len(self) < 10:
            super().add(passenger)
        else:
            print("Wagon is full")
