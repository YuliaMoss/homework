from hw11.cook import Cook


class Baking(Cook):
    def __init__(self, name: str, category: str):
        super().__init__(name, category)

    def cook(self):
        return "Baking"

    def is_prepared(self):
        return "The food will be prepared when it's done baking."
