from hw11.menu.fry.frying import Frying


class Fish(Frying):
    def __init__(self, name: str, category: str, fish_type: str, spices: str):
        super().__init__(name, category)
        self.fish_type = fish_type
        self.spices = spices

    def cook(self):
        print(f"Frying {self.name}")

    def is_prepared(self):
        print(f"The {self.name} will be prepared when it's done frying.")

    def add_spices(self):
        print(f"Marinating with {self.spices}")

    def all_info(self):
        print(f"{self.name}, {self.category}, {self.fish_type}, {self.spices}")
