from nose.tools import *
from tictactoe.game_controller import GameController

def ai_has_o_if_user_has_x_test():
    controller = GameController("X")
    assert_equal("O", controller._ai_symbol())

def ai_has_x_if_user_has_o_test():
    controller = GameController("O")
    assert_equal("X", controller._ai_symbol())

