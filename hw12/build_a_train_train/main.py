from hw12.build_a_train_train.train import Train
from hw12.build_a_train_train.wagon import Wagon


if __name__ == '__main__':
    new_wagon_1 = Wagon()
    new_wagon_2 = Wagon()
    new_wagon_3 = Wagon()
    new_wagon_4 = Wagon()

    new_train_1 = Train()
    new_train_1.add(new_wagon_1)
    new_train_1.add(new_wagon_2)
    new_train_1.add(new_wagon_3)
    new_train_1.add(new_wagon_4)

    new_train_1[0] = "пасажир Васа"
    new_train_1[1] = "пасажир Васа"
    new_train_1[1] = "пасажир Васа"
    new_train_1[1] = "пасажир Васа"
    new_train_1[1] = "пасажир Васа"
    new_train_1[1] = "пасажир Васа"
    new_train_1[1] = "пасажир Васа"
    new_train_1[1] = "пасажир Васа"
    new_train_1[1] = "пасажир Васа"
    new_train_1[1] = "пасажир Васа"
    new_train_1[1] = "пасажир Васа"
    # new_train_1[1] = "пасажир Васа"
    # new_train_1[1] = "пасажир Васа"
    print(f"Number of wagons: {len(new_train_1)}")

    new_train_1[2] = "пасажир Ірина"

    print(f"Number of passengers: {len(new_wagon_1)}")
    print(f"Number of passengers: {len(new_wagon_2)}")
    print(f"Number of passengers: {len(new_wagon_3)}")
    print(f"Number of passengers: {len(new_wagon_4)}")

    print(new_train_1.__str__())