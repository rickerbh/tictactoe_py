from nose.tools import *
from tictactoe.ai_player import AIPlayer
from collections import Counter
from tictactoe.game_board import GameBoard
from tictactoe.game_controller import GameController
import functools

def ai_player_makes_best_opening_move_test():
    controller = GameController("X")
    controller.make_ai_move()
    board = controller._board
    assert_equal(True, functools.reduce(_o_finder, board.corners, False))

def _o_finder(accum, item):
    if (accum):
        return accum
    return item == "O"

def ai_player_responds_to_opening_corner_test():
    controller = GameController("X")
    controller.play(0)
    controller.make_ai_move()
    board = controller._board
    assert_equal("O", board.center[0])
    
def ai_player_responds_to_opening_edge_test():
    controller = GameController("X")
    controller.play(1)
    controller.make_ai_move()
    board = controller._board
    assert_equal("O", board.center[0])

def ai_player_responds_to_opening_center_test():
    controller = GameController("X")
    controller.play(4)
    controller.make_ai_move()
    board = controller._board
    assert_equal(True, functools.reduce(_o_finder, board.corners, False))

def ai_player_checks_for_row_win_success_test():
    board = GameBoard()
    board.play_move("X", 0)
    board.play_move("X", 1)
    ai = AIPlayer("X", "O")
    assert_equal(True, ai.win_available(board))

def ai_player_checks_for_column_win_success_test():
    board = GameBoard()
    board.play_move("X", 1)
    board.play_move("X", 4)
    ai = AIPlayer("X", "O")
    assert_equal(True, ai.win_available(board))

def ai_player_checks_for_diagonal_win_success_test():
    board = GameBoard()
    board.play_move("X", 6)
    board.play_move("X", 4)
    ai = AIPlayer("X", "O")
    assert_equal(True, ai.win_available(board))

def ai_player_takes_win_if_available_in_row_test():
    board = GameBoard()
    board.play_move("X", 3)
    board.play_move("X", 5)
    ai = AIPlayer("X", "O")
    assert_equal(4, ai.take_win(board))
    
def ai_player_takes_win_if_available_in_column_test():
    board = GameBoard()
    board.play_move("X", 2)
    board.play_move("X", 8)
    ai = AIPlayer("X", "O")
    assert_equal(5, ai.take_win(board))

def ai_player_takes_win_if_available_in_diagonal_test():
    board = GameBoard()
    board.play_move("X", 4)
    board.play_move("X", 6)
    ai = AIPlayer("X", "O")
    assert_equal(2, ai.take_win(board))

def ai_player_checks_for_row_loss_success_test():
    board = GameBoard()
    board.play_move("O", 0)
    board.play_move("O", 1)
    ai = AIPlayer("X", "O")
    assert_equal(True, ai.loss_available(board))

def ai_player_checks_for_column_loss_success_test():
    board = GameBoard()
    board.play_move("O", 1)
    board.play_move("O", 4)
    ai = AIPlayer("X", "O")
    assert_equal(True, ai.loss_available(board))

def ai_player_checks_for_diagonal_loss_success_test():
    board = GameBoard()
    board.play_move("O", 0)
    board.play_move("O", 4)
    ai = AIPlayer("X", "O")
    assert_equal(True, ai.loss_available(board))

def ai_player_block_loss_if_available_in_row_test():
    board = GameBoard()
    board.play_move("O", 3)
    board.play_move("O", 5)
    ai = AIPlayer("X", "O")
    assert_equal(4, ai.block_loss(board))
    
def ai_player_block_loss_if_available_in_column_test():
    board = GameBoard()
    board.play_move("O", 2)
    board.play_move("O", 8)
    ai = AIPlayer("X", "O")
    assert_equal(5, ai.block_loss(board))

def ai_player_block_loss_if_available_in_diagonal_test():
    board = GameBoard()
    board.play_move("O", 4)
    board.play_move("O", 2)
    ai = AIPlayer("X", "O")
    assert_equal(6, ai.block_loss(board))

def ai_player_should_play_in_opposite_corner_test():
    board = GameBoard()
    board.play_move("O", 0)
    board.play_move("X", 4)
    ai = AIPlayer("X", "O")
    assert_equal(True, ai.should_take_opposite_corner(board))

def ai_player_should_take_opposite_corner_test():
    board = GameBoard()
    board.play_move("O", 0)
    board.play_move("X", 4)
    ai = AIPlayer("X", "O")
    assert_equal(8, ai.take_opposite_corner(board))

def ai_player_should_take_other_opposite_corner_test():
    board = GameBoard()
    board.play_move("O", 2)
    board.play_move("X", 4)
    ai = AIPlayer("X", "O")
    assert_equal(6, ai.take_opposite_corner(board))

def ai_player_check_for_corner_available_test():
    board = GameBoard()
    board.play_move("X", 0)
    board.play_move("O", 4)
    ai = AIPlayer("X", "O")
    assert_equal(True, ai.corner_available(board))

def ai_player_check_for_no_corners_available_test():
    board = GameBoard()
    board.play_move("X", 0)
    board.play_move("O", 2)
    board.play_move("X", 6)
    board.play_move("O", 8)
    ai = AIPlayer("X", "O")
    assert_equal(False, ai.corner_available(board))

def ai_player_should_take_corner_test():
    board = GameBoard()
    board.play_move("X", 0)
    board.play_move("O", 4)
    ai = AIPlayer("X", "O")
    move = ai.take_corner(board)
    result = move == 2 or move == 6 or move == 8
    assert_equal(True, result)

def ai_player_check_for_edge_available_test():
    board = GameBoard()
    board.play_move("X", 1)
    board.play_move("O", 3)
    ai = AIPlayer("X", "O")
    assert_equal(True, ai.edge_available(board))

def ai_player_check_for_no_edge_available_test():
    board = GameBoard()
    board.play_move("X", 1)
    board.play_move("O", 3)
    board.play_move("X", 5)
    board.play_move("O", 7)
    ai = AIPlayer("X", "O")
    assert_equal(False, ai.edge_available(board))

def ai_player_should_take_edge_test():
    board = GameBoard()
    board.play_move("X", 1)
    board.play_move("O", 5)
    ai = AIPlayer("X", "O")
    move = ai.take_edge(board)
    result = move == 7 or move == 3
    assert_equal(True, result)
