from abc import ABC, abstractmethod
from hw11.cook import Cook


class Boiling(Cook, ABC):
    def __init__(self, name: str, category: str):
        super().__init__(name, category)

    def cook(self):
        print(f"Boiling {self.name}")

    def serve(self):
        print(f"Serving {self.name}.")

    @abstractmethod
    def done_boiling(self):
        pass
