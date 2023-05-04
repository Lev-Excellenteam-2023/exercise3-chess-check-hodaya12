
from unittest.mock import Mock


import chess_engine
import Piece
from enums import Player

def board(l):
    board1=[[],[],[],[],[],[],[],[]]
    for i in range(7):
        for j in range(7):
            exist=False
            for t in l:
                if t.get_col_number()==j and t.get_row_number()==i:
                    board1[i].append(t)
                    exist=True
            if not exist:
                board1[i].append(Player.EMPTY)
    return board1

def test_empty_board():
        knight=Piece.Knight('knight test',3,4,Player.PLAYER_1)
        game=Mock()
        game.get_piece.return_value=Player.EMPTY
        peaceful_moves=knight.get_valid_peaceful_moves(game)
        expected_moves = {(1, 3), (1, 5), (2, 2), (2, 6), (4, 2), (4, 6), (5, 3), (5, 5)}
        assert set(peaceful_moves) == expected_moves




def test_almost_empty_board():
    game = Mock()
    mock_get_piece=Mock(side_effect=lambda row,col:game.board[row][col] if 0 <= row <= 7 and 0 <= col <= 7 else 0)
    game.get_piece=mock_get_piece
    game.board=board([Piece.Knight('knight_test', 3, 4, 'white'),Piece.Piece('king',4,3,'white'), \
                      Piece.Piece('rook', 4, 4, 'black'), Piece.Piece('king', 4, 5, 'black') ])
    peaceful_moves = game.get_piece(3, 4).get_valid_peaceful_moves(game)
    expected_moves = {(1, 3), (1, 5), (2, 2), (2, 6), (4, 2), (4, 6), (5, 3), (5, 5)}
    assert set(peaceful_moves) == expected_moves

def test_occupied_squares():
    game = Mock()
    #knight = Piece.Knight('knight test', 3, 4, Player.PLAYER_1)
    game.board = board([Piece.Knight('knight_test', 3, 4, Player.PLAYER_1), Piece.Piece('king',1,3,'black'),
                        Piece.Piece('rook', 2, 2, 'white'),Piece.Piece('king', 4, 2, 'white'), Piece.Piece('king', 5, 3, 'black')])
    mock_get_piece = Mock(side_effect=lambda row, col: game.board[row][col] if 0 <= row <= 7 and 0 <= col <= 7 else None)
    game.get_piece=mock_get_piece
    peaceful_moves=game.get_piece(3,4).get_valid_peaceful_moves(game)
    expected_moves = {(1, 5), (2, 6),  (4, 6),(5, 5)  }
    assert set(peaceful_moves) == expected_moves

def test_occupied_squares_for_piece_takes():
        game = Mock()
        game.board = board([Piece.Knight('knight_test', 3, 4, 'white'), Piece.Piece('king',1,3,'black') ,\
                            Piece.Piece('rook', 2, 2, 'white') ,Piece.Piece('king', 4, 2, 'white'),Piece.Piece('king', 5, 3, 'black')      ])
        mock_get_piece = Mock(
            side_effect=lambda row, col: game.board[row][col] if 0 <= row <= 7 and 0 <= col <= 7 else None)
        game.get_piece = mock_get_piece
        mock_is_valid=Mock(side_effect=lambda row,col:game.get_piece(row,col) is not None and game.get_piece(row,col)!=Player.EMPTY)
        game.is_valid_piece=mock_is_valid
        peaceful_moves=game.get_piece(3,4).get_valid_piece_takes(game)
        expected_moves = {(1, 3), (5,3)}
        assert set(peaceful_moves) == expected_moves

def test_empty_board_for_piece_takes():
        game = Mock()
        game.board = board([Piece.Knight('knight_test', 3, 4, Player.PLAYER_1)])
        mock_get_piece = Mock(
            side_effect=lambda row, col: game.board[row][col] if 0 <= row <= 7 and 0 <= col <= 7 else None)
        game.get_piece = mock_get_piece
        mock_is_valid = Mock(side_effect=lambda row, col: game.get_piece(row, col) is not None and game.get_piece(row,                                                                                                      col) != Player.EMPTY)
        game.is_valid_piece = mock_is_valid
        peaceful_moves=game.get_piece(3,4).get_valid_piece_takes(game)
        expected_moves = set()
        assert set(peaceful_moves) == expected_moves

def test_8_squares_for_piece_takes():
        game = Mock()
        game.board = board([Piece.Knight('knight_test', 3, 4, Player.PLAYER_1),Piece.Piece('rook', 1, 3, 'black'),\
        Piece.Piece('rook', 2, 2, 'black'),Piece.Piece('rook', 1, 5, 'black'),Piece.Piece('rook', 2, 6, 'black'), \
                            Piece.Piece('rook', 4, 2, 'black'),Piece.Piece('rook', 5, 3, 'black'),Piece.Piece('rook', 4, 6, 'black'),\
                            Piece.Piece('rook', 5, 5, 'black')])

        mock_get_piece = Mock(
            side_effect=lambda row, col: game.board[row][col] if 0 <= row <= 7 and 0 <= col <= 7 else None)
        game.get_piece = mock_get_piece
        mock_is_valid = Mock(side_effect=lambda row, col: game.get_piece(row, col) is not None and game.get_piece(row,
                                                                                                                  col) != Player.EMPTY)
        game.is_valid_piece = mock_is_valid
        peaceful_moves = game.get_piece(3, 4).get_valid_piece_takes(game)
        expected_moves = {(1,3),(2,2),(1,5),(2,6),(4,2),(5,3),(4,6),(5,5)}
        assert set(peaceful_moves) == expected_moves



