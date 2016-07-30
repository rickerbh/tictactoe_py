from nose.tools import *
from tictactoe.game_board import GameBoard
from tictactoe.game_state import GameState

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
    state = GameState(board)
    assert_equal(False, state.is_draw())
    board.play_move("X", 7)
    state = GameState(board)
    assert_equal(True, state.is_draw())

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
    state = GameState(board)
    assert_equal(True, state.has_winner())
    assert_equal(False, state.is_draw())

def game_is_won_on_a_diagonal_test():
    board = GameBoard()
    board.play_move("X", 2)
    state = GameState(board)
    assert_equal(False, state.has_winner())
    board.play_move("X", 4)
    state = GameState(board)
    assert_equal(False, state.has_winner())
    board.play_move("X", 6)
    state = GameState(board)
    assert_equal(True, state.has_winner())

def game_is_won_on_a_row_test():
    board = GameBoard()
    board.play_move("X", 3)
    state = GameState(board)
    assert_equal(False, state.has_winner())
    board.play_move("X", 4)
    state = GameState(board)
    assert_equal(False, state.has_winner())
    board.play_move("X", 5)
    state = GameState(board)
    assert_equal(True, state.has_winner())

def game_is_won_on_a_column_test():
    board = GameBoard()
    board.play_move("X", 1)
    state = GameState(board)
    assert_equal(False, state.has_winner())
    board.play_move("X", 4)
    state = GameState(board)
    assert_equal(False, state.has_winner())
    board.play_move("X", 7)
    state = GameState(board)
    assert_equal(True, state.has_winner())

def check_for_edge_available_test():
    board = GameBoard()
    board.play_move("X", 1)
    board.play_move("O", 3)
    state = GameState(board)
    assert_equal(True, state.edge_available())

def no_edge_available_test():
    board = GameBoard()
    board.play_move("X", 1)
    board.play_move("O", 3)
    board.play_move("X", 5)
    board.play_move("O", 7)
    state = GameState(board)
    assert_equal(False, state.edge_available())

def check_for_corner_available_test():
    board = GameBoard()
    board.play_move("X", 0)
    board.play_move("O", 4)
    state = GameState(board)
    assert_equal(True, state.corner_available())

def no_corners_available_test():
    board = GameBoard()
    board.play_move("X", 0)
    board.play_move("O", 2)
    board.play_move("X", 6)
    board.play_move("O", 8) 
    state = GameState(board)
    assert_equal(False, state.corner_available())

def row_win_success_test():
    board = GameBoard()
    board.play_move("X", 0)
    board.play_move("X", 1)
    assert_equal(True, GameState(board).win_available("X"))

def column_win_success_test():
    board = GameBoard()
    board.play_move("X", 1)
    board.play_move("X", 4)
    assert_equal(True, GameState(board).win_available("X"))

def diagonal_win_success_test():
    board = GameBoard()
    board.play_move("X", 6)
    board.play_move("X", 4)
    assert_equal(True, GameState(board).win_available("X"))

def random_corner_test():
    result = GameBoard().random_corner
    assert_equal(True, result in [0, 2, 6, 8])
