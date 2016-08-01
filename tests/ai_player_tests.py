from nose.tools import *
from unittest.mock import MagicMock
from tictactoe.ai_player import AIPlayer
from tictactoe.game_controller import GameController

def ai_play_notification_calls_controller_test():
    a = AIPlayer("X", "O")
    controller = GameController(a, a)
    controller._play = MagicMock()
    a.play_notification(controller)
    assert_equal(True, controller._play.called)
