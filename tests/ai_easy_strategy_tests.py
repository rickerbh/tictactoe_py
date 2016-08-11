from nose.tools import *
from tictactoe.ai_strategies.easy import Easy
from tictactoe.game_board import GameBoard

def makes_any_opening_move_test():
    ai = Easy("X", "O")
    board = GameBoard()
    move = ai.make_move(board)
    assert_equal(True, move in list(range(0, 9)))

def makes_move_in_nearly_full_board_test():
    ai = Easy("X", "O")
    board = GameBoard()
    board.play_move("X", 0)
    board.play_move("O", 2)
    board.play_move("X", 3)
    board.play_move("O", 4)
    board.play_move("X", 5)
    board.play_move("O", 6)
    board.play_move("X", 7)
    board.play_move("O", 8)
    assert_equal(1, ai.make_move(board))
    
