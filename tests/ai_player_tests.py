from nose.tools import *
from unittest.mock import MagicMock
from tictactoe.ai_player import AIPlayer
from tictactoe.ai_strategies.hard import Hard
from tictactoe.ai_strategies.easy import Easy
from tictactoe.game_controller import GameController
from tictactoe.player import Player

def ai_play_notification_calls_controller_test():
    a = AIPlayer("X", "O")
    b = AIPlayer("O", "X")
    controller = GameController(a, b, None, None)
    controller.notify_play = MagicMock()
    a.play_notification(controller)
    assert_equal(True, controller.notify_play.called)

def ai_player_has_perfect_strategy_by_default_test():
    player = AIPlayer("X", "O")
    assert_equal(True, isinstance(player.strategy, Hard))

def ai_player_can_set_strategy_test():
    player = AIPlayer("X", "O")
    easy = Easy("X", "O")
    player.strategy = easy
    assert_equal(True, isinstance(player.strategy, Easy))
