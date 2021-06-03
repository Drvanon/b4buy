from .player import Player
from .building import Building

class Game:
    def __init__(self):
        self.players = []
        self.buildings = []
        self.contracts = []
        self.orders = []

    def tick(self):
        for order in self.orders:
            order.execute()
        for building in self.buildings:
            building.produce()

    def add_player(self, player):
        self.players.append(player)

    def buy_building(self, player, position, scheme):
        if player.money < scheme['costs']['money']:
            return None

        building = Building(player, position, scheme)
        self.buildings.append(building)
        player.money -= scheme['costs']['money']
        return building

