class BaseWagon:
    def __init__(self):
        self.entities = []

    def add(self, entity):
        self.entities.append(entity)

    def __len__(self):
        return len(self.entities)
