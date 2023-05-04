import pytest
import chess_engine
import Piece
from enums import Player
import ai_engine

def test_evaluate_board():
    game=chess_engine.game_state()
    # Initialize White pieces
    white_rook_1 = Piece.Rook('r', 0, 0, Player.PLAYER_1)
    white_rook_2 = Piece.Rook('r', 0, 7, Player.PLAYER_1)
    white_knight_1 = Piece.Knight('n', 0, 1, Player.PLAYER_1)
    white_knight_2 = Piece.Knight('n', 0, 6, Player.PLAYER_1)
    white_bishop_1 = Piece.Bishop('b', 0, 2, Player.PLAYER_1)
    white_bishop_2 = Piece.Bishop('b', 0, 5, Player.PLAYER_1)
    white_queen = Piece.Queen('q', 0, 4, Player.PLAYER_1)
    white_king = Piece.King('k', 0, 3, Player.PLAYER_1)
    white_pawn_1 = Piece.Pawn('p', 1, 0, Player.PLAYER_1)
    white_pawn_2 = Piece.Pawn('p', 1, 1, Player.PLAYER_1)
    white_pawn_3 = Piece.Pawn('p', 1, 2, Player.PLAYER_1)
    white_pawn_4 = Piece.Pawn('p', 1, 3, Player.PLAYER_1)
    white_pawn_5 = Piece.Pawn('p', 1, 4, Player.PLAYER_1)
    white_pawn_6 = Piece.Pawn('p', 1, 5, Player.PLAYER_1)
    white_pawn_7 = Piece.Pawn('p', 1, 6, Player.PLAYER_1)
    white_pawn_8 = Piece.Pawn('p', 1, 7, Player.PLAYER_1)

    game.board = [
        [white_rook_1, white_knight_1, white_bishop_1, white_king, white_queen, white_bishop_2, white_knight_2,
         white_rook_2],
        [white_pawn_1, white_pawn_2, white_pawn_3, white_pawn_4, white_pawn_5, white_pawn_6, white_pawn_7,
         white_pawn_8],
        [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
         Player.EMPTY],
        [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
         Player.EMPTY],
        [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
         Player.EMPTY],
        [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
         Player.EMPTY],
        [Player.EMPTY,Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
         Player.EMPTY],
        [Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY, Player.EMPTY,
         Player.EMPTY]
    ]

    ai=ai_engine.chess_ai()
    assert ai.evaluate_board(game,Player.PLAYER_2)==1400