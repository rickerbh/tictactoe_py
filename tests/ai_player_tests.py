from nose.tools import *
from tictactoe.ai_player import AIPlayer
from tictactoe.game_board import GameBoard
import functools

def ai_player_makes_best_opening_move_test():
    ai = AIPlayer("X", "O")
    move = ai._make_opening_ai_move(GameBoard())
    result = move in GameBoard().corner_positions
    assert_equal(True, result)

def _o_finder(accum, item):
    if (accum):
        return accum
    return item == "O"

def ai_player_responds_to_opening_corner_test():
    board = GameBoard()
    board.play_move("X", 0)
    ai = AIPlayer("O", "X")
    result = ai._make_responding_ai_move(board)
    assert_equal(4, result)
    
def ai_player_responds_to_opening_edge_test():
    board = GameBoard()
    board.play_move("X", 1)
    ai = AIPlayer("O", "X")
    result = ai._make_responding_ai_move(board)
    assert_equal(4, result)

def ai_player_responds_to_opening_center_test():
    board = GameBoard()
    board.play_move("X", 4)
    ai = AIPlayer("O", "X")
    result = ai._make_responding_ai_move(board)
    assert_equal(True, result in [0, 2, 6, 8])
    
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

def ai_player_should_take_corner_test():
    board = GameBoard()
    board.play_move("X", 0)
    board.play_move("O", 4)
    ai = AIPlayer("X", "O")
    move = ai.take_corner(board)
    result = move == 2 or move == 6 or move == 8
    assert_equal(True, result)

def ai_player_should_take_edge_test():
    board = GameBoard()
    board.play_move("X", 1)
    board.play_move("O", 5)
    ai = AIPlayer("X", "O")
    move = ai.take_edge(board)
    result = move == 7 or move == 3
    assert_equal(True, result)
