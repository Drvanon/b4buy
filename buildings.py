class Building:
    def __init__(self, settings, building_type, position):
        self.building_type = building_type
        self.position = position

        self.stock = []

        sets = settings['buildings'][building_type]
        self.ins = sets.ins
        self.outs = sets.outs
        self.speed = sets.speed

        self.producing = False

        self.frames_since_last_produce = self.speed

        self.connections = []

    def produce(self):
        self.producing = True
        for in_item in self.ins:
            if in_item not in self.stock:
                self.producing = False
                break

        if self.producing:
            for in_item in self.ins:
                self.stock.remove(in_item)

class Connection:
    def __init__(self, distance, building1, building2):
        self.distance = distance
        self.buildings = (building1, building2)
        if not self in building1.connections:
            building1.connections.add_connection(self)
            building2.connections.add_connection(self)

    def destroy(self):
        self.buildings[0].connections.remove(self)
        self.buildings[1].connections.remove(self)
