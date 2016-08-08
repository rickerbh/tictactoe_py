from nose.tools import *
from tictactoe.ai_strategies.medium import Medium
from tictactoe.game_board import GameBoard

def medium_strategy_makes_any_opening_move_test():
    ai = Medium("X", "O")
    board = GameBoard()
    move = ai.make_move(board)
    assert_equal(True, move in list(range(0, 9)))
