import pytest
from unittest.mock import Mock

@pytest.fixture
def game():
    game = Mock()
    game.get_piece=Mock(side_effect=lambda row, col: game.board[row][col] if 0 <= row <= 7 and 0 <= col <= 7 else None)
    return game