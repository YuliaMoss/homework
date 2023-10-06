from hw11.menu.bake.baking import Baking


class Cake(Baking):
    def __init__(self, name: str, category: str, cake_type: str, decorations: list):
        super().__init__(name, category)
        self.cake_type = cake_type
        self.decorations = decorations

    def cook(self):
        print(f"Backing {self.name}")

    def is_prepared(self):
        print(f"The {self.name} cake is prepared and decorated.")

    def all_info(self):
        print(f"This {self.category} is {self.cake_type} and called {self.name}.")
        print(f"Decorations: {', '.join(self.decorations)}")
