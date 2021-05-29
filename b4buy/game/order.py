class Order:
    def __init__(self, building1, building2, products12, products21):
        self.building1 = building1
        self.building2 = building2
        self.products12 = products12
        self.products21 = products21

    def execute(self):
        if not building1.has_sufficient(products12) or not building2.has_sufficient(products21):
            return False
        for product, count in storage12.items():
            building1.storage[product] -= count
            building2.storage[product] += count
        for product, count in storage21.items():
            building2.storage[product] -= count
            building1.storage[product] += count
        return True
