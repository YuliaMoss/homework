from hw11.menu.fry.frying import Frying


class Meat(Frying):
    def __init__(self, name: str, category: str, meat_type: str, marinade: str):
        super().__init__(name, category)
        self.meat_type = meat_type
        self.marinade = marinade

    def cook(self):
        print(f"Frying {self.name}")

    def is_prepared(self):
        print(f"The {self.meat_type} will be prepared when it's done frying.")

    def marinate(self):
        print(f"Marinating with {self.marinade}")

    def all_info(self):
        print(f"{self.name}, {self.category}, {self.meat_type}, {self.marinade}")
