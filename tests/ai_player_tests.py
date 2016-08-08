from nose.tools import *
from unittest.mock import MagicMock
from tictactoe.ai_player import AIPlayer
from tictactoe.game_controller import GameController
from tictactoe.player import Player

def ai_play_notification_calls_controller_test():
    a = AIPlayer("X", "O")
    b = AIPlayer("O", "X")
    controller = GameController(a, b, None, None)
    controller.notify_play = MagicMock()
    a.play_notification(controller)
    assert_equal(True, controller.notify_play.called)
