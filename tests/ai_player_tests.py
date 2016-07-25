from nose.tools import *
from tictactoe.ai_player import AIPlayer
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
    
