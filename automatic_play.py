#
# The GUI engine for Python Chess
#
# Author: Boo Sung Kim, Eddie Sharick
# Note: The pygame tutorial by Eddie Sharick was used for the GUI engine. The GUI code was altered by Boo Sung Kim to
# fit in with the rest of the project.
#
import chess_engine
import pygame as py

import ai_engine
from enums import Player
import logging
import time
LOG_FORMAT="%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="logs",level=logging.DEBUG,filemode='w',format=LOG_FORMAT)
logger=logging.getLogger()


"""Variables"""
WIDTH = HEIGHT = 512  # width and height of the chess board
DIMENSION = 8  # the dimensions of the chess board
SQ_SIZE = HEIGHT // DIMENSION  # the size of each of the squares in the board
MAX_FPS = 15  # FPS for animations
IMAGES = {}  # images for the chess pieces
colors = [py.Color("white"), py.Color("gray")]

# TODO: AI black has been worked on. Mirror progress for other two modes
def load_images():
    '''
    Load images for the chess pieces
    '''
    for p in Player.PIECES:
        IMAGES[p] = py.transform.scale(py.image.load("images/" + p + ".png"), (SQ_SIZE, SQ_SIZE))


def draw_game_state(screen, game_state, valid_moves, square_selected):
    ''' Draw the complete chess board with pieces

    Keyword arguments:
        :param screen       -- the pygame screen
        :param game_state   -- the state of the current chess game
    '''
    draw_squares(screen)
    #highlight_square(screen, game_state, valid_moves, square_selected)
    draw_pieces(screen, game_state)


def draw_squares(screen):
    ''' Draw the chess board with the alternating two colors

    :param screen:          -- the pygame screen
    '''
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[(r + c) % 2]
            py.draw.rect(screen, color, py.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


def draw_pieces(screen, game_state):
    ''' Draw the chess pieces onto the board

    :param screen:          -- the pygame screen
    :param game_state:      -- the current state of the chess game
    '''
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = game_state.get_piece(r, c)
            if piece is not None and piece != Player.EMPTY:
                screen.blit(IMAGES[piece.get_player() + "_" + piece.get_name()],
                            py.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


def highlight_square(screen, game_state, valid_moves, square_selected):
    if square_selected != () and game_state.is_valid_piece(square_selected[0], square_selected[1]):
        row = square_selected[0]
        col = square_selected[1]

        if (game_state.whose_turn() and game_state.get_piece(row, col).is_player(Player.PLAYER_1)) or \
                (not game_state.whose_turn() and game_state.get_piece(row, col).is_player(Player.PLAYER_2)):
            # hightlight selected square
            s = py.Surface((SQ_SIZE, SQ_SIZE))
            s.set_alpha(100)
            s.fill(py.Color("blue"))
            screen.blit(s, (col * SQ_SIZE, row * SQ_SIZE))

            # highlight move squares
            s.fill(py.Color("green"))

            for move in valid_moves:
                screen.blit(s, (move[1] * SQ_SIZE, move[0] * SQ_SIZE))


def main():

    turn='w'
    py.init()
    screen = py.display.set_mode((WIDTH, HEIGHT))
    clock = py.time.Clock()
    #game_state = chess_engine.game_state()
    load_images()
    running = True
    square_selected = ()  # keeps track of the last selected square
    player_clicks = []  # keeps track of player clicks (two tuples)
    valid_moves = []
    game_over = False

    ai = ai_engine.chess_ai()
    game_state = chess_engine.game_state()
    t = 0
    white_turns=0
    black_turns=0
    checks=0
    knight_steps=0
    is_checked=False


    while running:

        str1 = ''
        for i in range(0,8):
            for j in range(0, 8):
                if game_state.is_valid_piece(i,j):
                    piece2=game_state.get_piece(i,j)
                    if piece2.is_player(Player.PLAYER_1):
                        str1+='white'
                    else:
                        str1+='black'
                    if piece2.get_name()=='k':
                        if piece2.is_player(Player.PLAYER_1):
                            king_location_w=(piece2.get_row_number(),piece2.get_col_number())
                        if piece2.is_player(Player.PLAYER_2):
                            king_location_b=(piece2.get_row_number(),piece2.get_col_number())
                        str1+=" king\n"
                    if piece2.get_name() == 'r':
                        str1 += " rook\n"
                    if piece2.get_name()=='n':
                        str1 += " knight\n"
                    if piece2.get_name()=='b':
                        str1 += " bishop\n"
                    if piece2.get_name()=='q':
                        str1 += " queen\n"
                    if piece2.get_name()=='p':
                        str1 += " pawn\n"

        logger.info("all the tools in this level: \n"+str1)
        check_for_check=game_state.check_for_check(king_location_w,Player.PLAYER_1)[0]
        check_for_check=check_for_check+game_state.check_for_check(king_location_b, Player.PLAYER_2)[0]
        if not is_checked and check_for_check:
            is_checked=True
            checks=checks+1
        if is_checked and not check_for_check:
            is_checked=False

        if not game_over:
            if not game_state.whose_turn():
                ai_move = ai.minimax_black(game_state, 3, -100000, 100000, False, Player.PLAYER_2)
                piece1 = game_state.get_piece(ai_move[0][0], ai_move[0][1])
                if piece1.is_player(Player.PLAYER_1):
                    white_turns = white_turns + 1
                    if t == 0:
                        logger.info("white started")
                else:
                    black_turns = black_turns + 1
                    if t == 0:
                        logger.info("black started")
                t = t + 1
                game_state.move_piece(ai_move[0], ai_move[1], True)
                if piece1.get_name()=='n':
                    knight_steps=knight_steps+1
            else:
                ai_move = ai.minimax_black(game_state, 3, -100000, 100000, True, Player.PLAYER_1)
                piece1 = game_state.get_piece(ai_move[0][0], ai_move[0][1])
                if piece1.is_player(Player.PLAYER_1):
                    white_turns = white_turns + 1
                    if t == 0:
                        logger.info("white started")
                else:
                    black_turns = black_turns + 1
                    if t == 0:
                        logger.info("black started")
                t = t + 1
                game_state.move_piece(ai_move[0], ai_move[1], True)
                if piece1.get_name()=='n':
                    knight_steps=knight_steps+1

        else:
            logger.info("white turns: "+str(white_turns))
            logger.info("black turns: " + str(black_turns))
            logger.info("number of checks: " + str(checks))
            logger.info("number of knight steps: " + str(knight_steps))
            break
        draw_game_state(screen, game_state, valid_moves, square_selected)
        endgame = game_state.checkmate_stalemate_checker()
        if endgame == 0:
            game_over = True
            logger.info("black wins")
            draw_text(screen, "Black wins.")
        elif endgame == 1:
            game_over = True
            logger.info("white wins")
            draw_text(screen, "White wins.")
        elif endgame == 2:
            game_over = True
            logger.info("Stalemate.")
            draw_text(screen, "Stalemate.")

        clock.tick(MAX_FPS)
        py.display.flip()


    # elif human_player is 'w':
    #     ai = ai_engine.chess_ai()
    #     game_state = chess_engine.game_state()
    #     valid_moves = []
    #     while running:
    #         for e in py.event.get():
    #             if e.type == py.QUIT:
    #                 running = False
    #             elif e.type == py.MOUSEBUTTONDOWN:
    #                 if not game_over:
    #                     location = py.mouse.get_pos()
    #                     col = location[0] // SQ_SIZE
    #                     row = location[1] // SQ_SIZE
    #                     if square_selected == (row, col):
    #                         square_selected = ()
    #                         player_clicks = []
    #                     else:
    #                         square_selected = (row, col)
    #                         player_clicks.append(square_selected)
    #                     if len(player_clicks) == 2:
    #                         if (player_clicks[1][0], player_clicks[1][1]) not in valid_moves:
    #                             square_selected = ()
    #                             player_clicks = []
    #                             valid_moves = []
    #                         else:
    #                             game_state.move_piece((player_clicks[0][0], player_clicks[0][1]),
    #                                                   (player_clicks[1][0], player_clicks[1][1]), False)
    #                             square_selected = ()
    #                             player_clicks = []
    #                             valid_moves = []
    #
    #                             ai_move = ai.minimax(game_state, 3, -100000, 100000, True, Player.PLAYER_2)
    #                             game_state.move_piece(ai_move[0], ai_move[1], True)
    #                     else:
    #                         valid_moves = game_state.get_valid_moves((row, col))
    #                         if valid_moves is None:
    #                             valid_moves = []
    #             elif e.type == py.KEYDOWN:
    #                 if e.key == py.K_r:
    #                     game_over = False
    #                     game_state = chess_engine.game_state()
    #                     valid_moves = []
    #                     square_selected = ()
    #                     player_clicks = []
    #                     valid_moves = []
    #                 elif e.key == py.K_u:
    #                     game_state.undo_move()
    #                     print(len(game_state.move_log))
    #         draw_game_state(screen, game_state, valid_moves, square_selected)
    #
    #         endgame = game_state.checkmate_stalemate_checker()
    #         if endgame == 0:
    #             game_over = True
    #             draw_text(screen, "Black wins.")
    #         elif endgame == 1:
    #             game_over = True
    #             draw_text(screen, "White wins.")
    #         elif endgame == 2:
    #             game_over = True
    #             draw_text(screen, "Stalemate.")
    #
    #         clock.tick(MAX_FPS)
    #         py.display.flip()
    #
    # elif human_player is 'b':
    #     pass


def draw_text(screen, text):
    font = py.font.SysFont("Helvitca", 32, True, False)
    text_object = font.render(text, False, py.Color("Black"))
    text_location = py.Rect(0, 0, WIDTH, HEIGHT).move(WIDTH / 2 - text_object.get_width() / 2,
                                                      HEIGHT / 2 - text_object.get_height() / 2)
    screen.blit(text_object, text_location)


if __name__ == "__main__":
    main()
