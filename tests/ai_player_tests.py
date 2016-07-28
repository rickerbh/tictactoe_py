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
    board.play_move("X", 0)
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
    board.play_move("X", 2)
    ai = AIPlayer("X", "O")
    assert_equal(6, ai.take_win(board))

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

