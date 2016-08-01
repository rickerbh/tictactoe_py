from nose.tools import *
from tictactoe.player import Player
from tictactoe.game_controller import GameController

def player_has_play_notification_test():
    result = None
    try:
        Player("X").play_notification(GameController("X", "O"))
    except NotImplementedError as ex:
        result = ex

    assert_equal(True, isinstance(result, NotImplementedError))

def player_has_symbol_test():
    player = Player("X")
    assert_equal("X", player.symbol)
