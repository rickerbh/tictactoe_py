from nose.tools import *
from unittest.mock import MagicMock
from tictactoe.human_player import HumanPlayer

def human_player_uses_writer_test():
    player = HumanPlayer("X", None)
    player._writer = MagicMock()
    player.play_notification(None)
    player._writer.assert_called_with()
    
