from abc import ABC, abstractmethod


class Cook(ABC):
    def __init__(self, name: str, category: str):
        self.name = name
        self.category = category

    @abstractmethod
    def cook(self):
        pass

    @abstractmethod
    def serve(self):
        pass


