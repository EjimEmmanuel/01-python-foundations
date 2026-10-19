import pytest

from stone_lines.game import Game
from stone_lines.player import Player


@pytest.fixture
def game():
    return Game(Player("Emma", "X"), Player("Chioma", "O"))
