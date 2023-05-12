


import chess_engine

def test_fools_mate():
    game = chess_engine.game_state()
    game.move_piece((1, 2), (2, 2), False)
    game.move_piece((6, 3), (4, 3), False)
    game.move_piece((1, 1), (3, 1), False)
    game.move_piece((7, 4), (3, 0), False)
    assert game.checkmate_stalemate_checker() == 0
