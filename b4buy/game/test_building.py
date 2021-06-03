import pytest
from .player import Player
from .building import Building
from collections import defaultdict

@pytest.fixture
def simple_scheme():
    return {
        'educts': {
            'e1': 1,
            'e2': 2
        },
        'products': {
            'p1': 1,
            'p2': 2,
        }
    }

@pytest.fixture
def player():
    return Player()

@pytest.fixture
def position():
    return (10, 100)

def test_building_creation(player, position, simple_scheme):
    building = Building(player, position, simple_scheme)
    assert building.owner == player
    assert building.scheme == simple_scheme
    assert building in player.buildings
    for count in building.storage.values():
        assert count == 0
    assert building.position == position

def test_has_sufficient(player, position, simple_scheme):
    building = Building(player, position, simple_scheme)

    building.storage = defaultdict(int, {
        "e1": 5,
        "e2": 6
    })
    assert building.has_sufficient(building.scheme['educts'])

    building.storage = defaultdict(int, {
        "e1": 1,
        "e2": 2
    })
    assert building.has_sufficient(building.scheme['educts'])

    building.storage = defaultdict(int, {
        "e1": 1,
        "e2": 1
    })
    assert not building.has_sufficient(building.scheme['educts'])

    scheme = {
        "non-existant": 1
    }
    assert not building.has_sufficient(scheme)


def test_produce(player, position, simple_scheme):
    building = Building(player, position, simple_scheme)
    assert not building.produce()
    for count in building.storage.values():
        assert count == 0

    building.storage = defaultdict(int, {
        "e1": 1,
        "e2": 2
    })
    building.produce()
    assert building.storage.get("e1") == 0
    assert building.storage.get("e2") == 0
    assert building.storage.get("p1") == 1
    assert building.storage.get("p2") == 2

