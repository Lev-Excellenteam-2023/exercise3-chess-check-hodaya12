import pytest
import chess_engine
from Piece import Knight, Piece
from unittest.mock import Mock
from enums import Player

def test_get_valid_piece_moves(game):
    game.board = [[Player.EMPTY] * 8 for _ in range(8)]
    game.board[3][4] = Knight('knight_test', 3, 4, 'white')
    game.board[2][2] = Piece('rook', 2, 2, 'white')
    game.board[1][5] = Piece('rook', 1, 5, 'white')
    game.board[2][6] = Piece('rook', 2, 6, 'white')
    game.board[4][2] = Piece('rook', 4, 2, 'black')
    game.board[5][3] = Piece('rook', 5, 3, 'black')
    game.board[4][6] = Piece('rook', 4, 6, 'black')
    game.board[5][5] = Piece('rook', 5, 5, 'black')
    mock_is_valid = Mock(
        side_effect=lambda row, col: game.get_piece(row, col) is not None and game.get_piece(row, col) != Player.EMPTY)
    game.is_valid_piece = mock_is_valid
    peaceful_moves = game.get_piece(3, 4).get_valid_piece_moves(game)
    expected_moves = {(1,3), (4, 2), (4, 6), (5, 3), (5, 5)}
    assert set(peaceful_moves) == expected_moves