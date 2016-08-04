from nose.tools import *
from tictactoe.board_stringification import BoardStringification
from tictactoe.game_board import GameBoard

def format_empty_row_test():
    player = BoardStringification()
    assert_equal("   |   |  \n", player.print_row(["", "", ""]))

def format_row_test():
    player = BoardStringification()
    assert_equal(" X | O | X\n", player.print_row(["X", "O", "X"]))

def format_spacer_test():
    player = BoardStringification()
    assert_equal("---+---+---\n", player.print_spacer())
    
def pretty_printed_game_test():
    player = BoardStringification()
    assert_equal("   |   |  \n---+---+---\n   |   |  \n---+---+---\n   |   |  \n", player.print_game_positions(GameBoard()))

    
