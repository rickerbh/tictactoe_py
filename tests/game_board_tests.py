from nose.tools import *
from tictactoe.game_board import GameBoard

def game_board_is_empty_on_creation_test():
    board = GameBoard()
    current_positions = board.positions
    assert_equal(["", "", "", "", "", "", "", "", ""], current_positions)

def game_board_registers_initial_move_test():
    board = GameBoard()
    board.play_move("X", 3)
    current_positions = board.positions
    assert_equal(["", "", "", "X", "", "", "", "", ""], current_positions)

def game_board_raises_exception_when_playing_invalid_positions_test():
    board = GameBoard()
    ex1 = None
    ex2 = None
    
    try:
        board.play_move("X", -1)
    except ValueError as ex:
        ex1 = ex

    try:
        board.play_move("O", 100)
    except ValueError as ex:
        ex2 = ex

    assert_equal('-1 is not a valid board position', ex1.args[0]) 
    assert_equal('100 is not a valid board position', ex2.args[0])

def game_board_raises_exception_when_playing_a_position_already_played_test():
    board = GameBoard()
    ex1 = None

    board.play_move("X", 2)

    try:
        board.play_move("X", 2)
    except ValueError as ex:
        ex1 = ex

    assert_equal('2 is already taken', ex1.args[0])

def game_is_won_on_a_row_test():
    board = GameBoard()
    board.play_move("X", 3)
    assert_equal(False, board.has_winner())
    board.play_move("X", 4)
    assert_equal(False, board.has_winner())
    board.play_move("X", 5)
    assert_equal(True, board.has_winner())

def game_is_won_on_a_column_test():
    board = GameBoard()
    board.play_move("X", 1)
    assert_equal(False, board.has_winner())
    board.play_move("X", 4)
    assert_equal(False, board.has_winner())
    board.play_move("X", 7)
    assert_equal(True, board.has_winner())

def game_is_won_on_a_diagonal_test():
    board = GameBoard()
    board.play_move("X", 2)
    assert_equal(False, board.has_winner())
    board.play_move("X", 4)
    assert_equal(False, board.has_winner())
    board.play_move("X", 6)
    assert_equal(True, board.has_winner())

def game_raises_exception_when_making_a_move_and_the_game_is_won_test():
    board = GameBoard()
    board.play_move("X", 3)
    board.play_move("X", 4)
    board.play_move("X", 5)
    ex1 = None
    try:
        board.play_move("X", 0)
    except ValueError as ex:
        ex1 = ex

    assert_equal('Game is over', ex1.args[0])

def reset_game_test():
    board = GameBoard()
    board.play_move("X", 0)
    board.reset()
    current_state = board.positions
    assert_equal(["", "", "", "", "", "", "", "", ""], current_state)

def game_is_draw_test():
    board = GameBoard()
    board.play_move("X", 0)
    board.play_move("O", 4)
    board.play_move("X", 2)
    board.play_move("O", 1)
    board.play_move("X", 6)
    board.play_move("O", 3)
    board.play_move("X", 5)
    board.play_move("O", 8)
    assert_equal(False, board.is_draw())
    board.play_move("X", 7)
    assert_equal(True, board.is_draw())

def won_games_arent_drawn_test():
    board = GameBoard()
    board.play_move("X", 0)
    board.play_move("O", 3)
    board.play_move("X", 1)
    board.play_move("O", 6)
    board.play_move("X", 5)
    board.play_move("O", 4)
    board.play_move("X", 8)
    board.play_move("O", 7)
    board.play_move("X", 2)
    assert_equal(True, board.has_winner())
    assert_equal(False, board.is_draw())
