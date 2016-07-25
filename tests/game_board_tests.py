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

def reset_game_test():
    board = GameBoard()
    board.play_move("X", 0)
    board.reset()
    current_state = board.positions
    assert_equal(["", "", "", "", "", "", "", "", ""], current_state)

def edges_test():
    board = GameBoard()
    board.play_move("1", 1)
    board.play_move("2", 3)
    board.play_move("3", 5)
    board.play_move("4", 7)
    assert_equal(["1", "2", "3", "4"], board.edges)

def corners_test():
    board = GameBoard()
    board.play_move("1", 0)
    board.play_move("2", 2)
    board.play_move("3", 6)
    board.play_move("4", 8)
    assert_equal(["1", "2", "3", "4"], board.corners)

def center_test():
    board = GameBoard()
    board.play_move("1", 4)
    assert_equal(["1"], board.center)

    
