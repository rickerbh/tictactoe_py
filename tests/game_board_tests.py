from nose.tools import *
from tictactoe.game_board import GameBoard

def game_board_is_empty_on_creation_test():
    board = GameBoard()
    current_state = board.game_state
    assert_equal(["", "", "", "", "", "", "", "", ""], current_state)

def game_board_registers_initial_move_test():
    board = GameBoard()
    board.play_move("X", 3)
    current_state = board.game_state
    assert_equal(["", "", "", "X", "", "", "", "", ""], current_state)

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
    assert_equal(None, board.winner())
    board.play_move("X", 4)
    assert_equal(None, board.winner())
    board.play_move("X", 5)
    assert_equal(True, board.has_winner())
    assert_equal("X", board.winner())

def game_raises_exception_when_making_a_move_and_the_game_is_won():
    assert_equal(False, "Complete me")
 
