class Building:
    def __init__(self, owner, position, scheme):
        self.owner = owner
        self.position = position
        self.scheme = scheme
        self.storage = {}

    def has_sufficient(self, items):
        for item, count in items.items():
            if self.storage[item] < count:
                return false
        return True

    def produce(self):
        if not self.has_sufficient(self.scheme.educts):
            return False

        for educt, count in self.scheme.educts.items():
            self.storage[educt] -= count

        for product, count in self.scheme.products.items():
            self.storage[product] += count
        return True

