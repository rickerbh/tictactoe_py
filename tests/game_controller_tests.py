from nose.tools import *
from unittest.mock import MagicMock
from tictactoe.game_board import GameBoard
from tictactoe.game_controller import GameController
from tictactoe.player import Player

def first_move_played_test():
    a = Player("X")
    a.play_notification = MagicMock()
    b = Player("O")
    controller = GameController(a, b, None, None)

    controller.notify_play()

    a.play_notification.assert_called_with(controller)

def second_move_played_test():
    a = Player("X")
    b = Player("O")
    b.play_notification = MagicMock()
    controller = GameController(a, b, None, None)
    board = GameBoard()
    board.play_move("X", 0)
    controller._board = board

    controller.notify_play()
    
    b.play_notification.assert_called_with(controller)
    
def place_move_test():
    a = Player("X")
    b = Player("O")
    b.play_notification = MagicMock()
    controller = GameController(a, b, None, None)

    controller.place_move(a, 8)

    assert_equal(8, controller._board.positions.index("X"))
    b.play_notification.assert_called_with(controller)
    
def reset_board_test():
    a = Player("X")
    b = Player("O")
    b.play_notification = MagicMock()
    controller = GameController(a, b, None, None)

    controller.place_move(a, 8)
    controller.reset()
    positions = controller._board.positions
    open_positions = len(list(filter(lambda x: x == "", controller._board.positions)))
    assert_equal(len(positions), open_positions)
