from nose.tools import *
from tictactoe.ai_strategy import AIStrategy
from tictactoe.game_board import GameBoard
import functools
import itertools

def ai_player_makes_best_opening_move_test():
    ai = AIStrategy("X", "O")
    move = ai._make_opening_ai_move(GameBoard())
    result = move in GameBoard().corner_positions
    assert_equal(True, result)

def _o_finder(accum, item):
    if (accum):
        return accum
    return item == "O"

def ai_player_responds_to_opening_corner_test():
    for move in GameBoard().corner_positions:
        board = GameBoard()
        board.play_move("X", move)
        ai = AIStrategy("O", "X")
        result = ai._make_responding_ai_move(board)
        assert_equal(4, result)
    
def ai_player_responds_to_opening_edge_test():
    board = GameBoard()
    for move in board.edge_positions:
        board.play_move("X", move)
        ai = AIStrategy("O", "X")
        result = ai._make_responding_ai_move(board)
        assert_equal(4, result)

def ai_player_responds_to_opening_center_test():
    board = GameBoard()
    board.play_move("X", board.center_position)
    ai = AIStrategy("O", "X")
    result = ai._make_responding_ai_move(board)
    assert_equal(True, result in [0, 2, 6, 8])
    
def ai_player_takes_win_if_available_in_row_test():
    for row in [[0, 1, 2], [3, 4, 5], [6, 7, 8]]:
        permutations = itertools.permutations(row)
        for option in permutations:
            board = GameBoard()
            board.play_move("X", option[0])
            board.play_move("X", option[1])
            ai = AIStrategy("X", "O")
            assert_equal(option[2], ai.take_win(board))
    
def ai_player_takes_win_if_available_in_column_test():
    for column in [[0, 3, 6], [1, 4, 7], [2, 5, 8]]:
        permutations = itertools.permutations(column)
        for option in permutations:
            board = GameBoard()
            board.play_move("X", option[0])
            board.play_move("X", option[1])
            ai = AIStrategy("X", "O")
            assert_equal(option[2], ai.take_win(board))

def ai_player_takes_win_if_available_in_diagonal_test():
    for diagonal in [[0, 4, 8], [2, 4, 6]]:
        permutations = itertools.permutations(diagonal)
        for option in permutations:
            board = GameBoard()
            board.play_move("X", option[0])
            board.play_move("X", option[1])
            ai = AIStrategy("X", "O")
            assert_equal(option[2], ai.take_win(board))

def ai_player_block_loss_if_available_in_row_test():
    for row in [[0, 1, 2], [3, 4, 5], [6, 7, 8]]:
        permutations = itertools.permutations(row)
        for option in permutations:
            board = GameBoard()
            board.play_move("O", option[0])
            board.play_move("O", option[1])
            ai = AIStrategy("X", "O")
            assert_equal(option[2], ai.block_loss(board))
    
def ai_player_block_loss_if_available_in_column_test():
    for column in [[0, 3, 6], [1, 4, 7], [2, 5, 8]]:
        permutations = itertools.permutations(column)
        for option in permutations:
            board = GameBoard()
            board.play_move("O", option[0])
            board.play_move("O", option[1])
            ai = AIStrategy("X", "O")
            assert_equal(option[2], ai.block_loss(board))

def ai_player_block_loss_if_available_in_diagonal_test():
    for diagonal in [[0, 4, 8], [2, 4, 6]]:
        permutations = itertools.permutations(diagonal)
        for option in permutations:
            board = GameBoard()
            board.play_move("O", option[0])
            board.play_move("O", option[1])
            ai = AIStrategy("X", "O")
            assert_equal(option[2], ai.block_loss(board))

def ai_player_should_play_in_opposite_corner_test():
    for corner in GameBoard().corner_positions:
        board = GameBoard()
        board.play_move("X", board.center_position)
        board.play_move("O", corner)
        ai = AIStrategy("X", "O")
        print("Placed in {0}".format(corner))
        assert_equal(True, ai.should_take_opposite_corner(board))

def ai_player_should_take_opposite_corner_test():
    for corner in [[0, 8], [2, 6]]:
        permutations = itertools.permutations(corner)
        for option in permutations:
            board = GameBoard()
            board.play_move("O", option[0])
            board.play_move("X", 4)
            ai = AIStrategy("X", "O")
            assert_equal(option[1], ai.take_opposite_corner(board))

def ai_player_take_corner_test():
    for corner in GameBoard().corner_positions:
        board = GameBoard()
        board.play_move("X", corner)
        board.play_move("O", 4)
        ai = AIStrategy("X", "O")
        move = ai.take_corner(board)
        result = move in GameBoard().corner_positions
        assert_equal(True, result)

def ai_player_take_edge_test():
    permutations = itertools.permutations(GameBoard().edge_positions)
    for option in permutations:
        board = GameBoard()
        board.play_move("O", option[0])
        board.play_move("X", option[1])
        board.play_move("O", option[2])
        ai = AIStrategy("X", "O")
        move = ai.take_edge(board)
        assert_equal(move, option[3])
