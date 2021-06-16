import pytest

from datetime import datetime
from .contract import Contract
from .game import Game
from .order import Order
from .player import Player

@pytest.fixture
def player1():
    return Player()

@pytest.fixture
def player2():
    return Player()

@pytest.fixture
def game():
    return Game()

@pytest.fixture
def building1(game, player1):
    scheme = {
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
    position = (10, 15)
    return game.buy_building(player1, position, scheme)

@pytest.fixture
def building2(game, player2):
    scheme = {
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
    position = (10, 15)
    return game.buy_building(player2, position, scheme)


def test_contract_init(freezer, player1, player2, building1, building2):
    money_transfer = 100
    end_date = datetime(2021, 7, 1)
    freezer.move_to('2021-06-16')
    frequency = 1
    order = Order(building1, building2, {}, {})
    contract = Contract(player1, player2, money_transfer, order, frequency, end_date)
    assert contract.start_date == datetime.now()
    assert contract.end_date == end_date
    assert contract.player1 == player1
    assert contract.player2 == player2
    assert contract.money_transfer == money_transfer
    assert contract.frequency == frequency
    assert contract.order == order
    assert contract.completed == False


