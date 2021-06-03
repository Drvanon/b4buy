import pytest
from .game import Game
from .building import Building
from .order import Order
from .player import Player

@pytest.fixture
def position():
    return (10, 40)

@pytest.fixture
def scheme():
    return {
        'costs': {
            'money': 100
        },
        'name': 'building1',
        'educts': {
            'e1': 1,
            'e2': 2
        },
        'products': {
            'p1': 1,
            'p2': 2
        }
    }

@pytest.fixture
def player():
    return Player()

@pytest.fixture
def game():
    return Game()

def test_game_init():
    game = Game()
    assert game.players == []
    assert game.buildings == []
    assert game.contracts == []
    assert game.orders == []

def test_game_add_player(game, player):
    game.add_player(player)
    assert player in game.players

def test_game_create_building(game, player, position, scheme):
    game.players += [player]
    player.money = 100
    building = game.buy_building(player, position, scheme)
    assert building in game.buildings
    assert player.money == 0

    building_too_expensive = game.buy_building(player, position, scheme)
    assert building_too_expensive == None
    assert player.money == 0

def test_game_tick(mocker, game, position, scheme):
    player1 = Player()
    player1.money = 200
    player2 = Player()
    player2.money = 100

    game.add_player(player1)
    game.add_player(player2)


    produce_mock = mocker.patch.object(Building, "produce")
    game.buy_building(player1, position, scheme)
    game.buy_building(player1, position, scheme)
    game.buy_building(player2, position, scheme)

    execute_mock = mocker.patch.object(Order, "execute")
    game.orders += [
            Order(game.buildings[0], game.buildings[1], {'p1': 1}, {'p2': 2}),
            Order(game.buildings[1], game.buildings[2], {'p1': 1}, {'p2': 2}),
            Order(game.buildings[2], game.buildings[0], {'p1': 1}, {'p2': 2}),
    ]

    game.tick()
    assert execute_mock.call_count == len(game.orders)
    assert produce_mock.call_count == len(game.buildings)

