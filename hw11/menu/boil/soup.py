from hw11.menu.boil.boiling import Boiling


class Soup(Boiling):
    def __init__(self, name: str, category: str, preparation_time: int, ingredients: list):
        super().__init__(name, category)
        self.preparation_time = preparation_time
        self.ingredients = ingredients

    def cook(self):
        print(f"Boiling {self.name}")

    def is_prepared(self):
        print(f"The {self.name} is prepared when the ingredients are cooked.")

    def get_ingredients(self):
        print(', '.join(self.ingredients))

    def all_info(self):
        print(f"{self.name}, {self.category}, {self.preparation_time}, {self.ingredients}")
