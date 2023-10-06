from hw11.menu.boil.boiling import Boiling


class Porridge(Boiling):
    def __init__(self, name: str, category: str, preparation_time: int, water_level: int):
        super().__init__(name, category)
        self.preparation_time = preparation_time
        self.water_level = water_level

    def cook(self):
        print(f"Boiling {self.name}")

    def is_prepared(self):
        print(f"Cook {self.name} while there is water.")

    def get_water_level(self):
        print(f"{self.water_level}")

    def all_info(self):
        print(f"{self.name}, {self.category}, {self.preparation_time}, {self.water_level}")
