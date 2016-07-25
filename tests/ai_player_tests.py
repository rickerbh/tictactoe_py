from nose.tools import *
from tictactoe.ai_player import AIPlayer
from tictactoe.game_controller import GameController

def ai_player_makes_best_opening_move_test():
    import functools
    controller = GameController("X")
    controller.make_ai_move()
    board = controller._board
    corners = [board.positions[i] for i in [0, 2, 6, 8]]
    def o_finder(accum, item):
        if (accum):
            return accum
        return item == "O"
    assert_equal(True, functools.reduce(o_finder, corners, False))
    
