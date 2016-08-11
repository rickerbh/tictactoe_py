from nose.tools import *
from tictactoe.ai_strategies.hard import Hard
from tictactoe.game_board import GameBoard
from tictactoe.game_state import GameState
import functools
import itertools

def makes_opening_move_in_corner_test():
    ai = Hard("X", "O")
    move = ai.make_move(GameBoard())
    result = move in GameBoard().corner_positions
    assert_equal(True, result)

def responds_to_opening_corner_with_center_test():
    for move in GameBoard().corner_positions:
        board = GameBoard()
        board.play_move("X", move)
        ai = Hard("O", "X")
        result = ai.make_move(board)
        assert_equal(board.center_position, result)
    
def responds_to_opening_edge_with_center_test():
    for move in GameBoard().edge_positions:
        board = GameBoard()
        board.play_move("X", move)
        ai = Hard("O", "X")
        result = ai.make_move(board)
        assert_equal(board.center_position, result)

def responds_to_opening_center_with_corner_test():
    board = GameBoard()
    board.play_move("X", board.center_position)
    ai = Hard("O", "X")
    result = ai._make_responding_ai_move(board)
    assert_equal(True, result in board.corner_positions)
    
def takes_win_if_available_in_row_test():
    for row in [[0, 1, 2], [3, 4, 5], [6, 7, 8]]:
        permutations = itertools.permutations(row)
        for option in permutations:
            board = GameBoard()
            board.play_move("X", option[0])
            board.play_move("X", option[1])
            ai = Hard("X", "O")
            assert_equal(option[2], ai.take_win(board))
    
def takes_win_if_available_in_column_test():
    for column in [[0, 3, 6], [1, 4, 7], [2, 5, 8]]:
        permutations = itertools.permutations(column)
        for option in permutations:
            board = GameBoard()
            board.play_move("X", option[0])
            board.play_move("X", option[1])
            ai = Hard("X", "O")
            assert_equal(option[2], ai.take_win(board))

def takes_win_if_available_in_diagonal_test():
    for diagonal in [[0, 4, 8], [2, 4, 6]]:
        permutations = itertools.permutations(diagonal)
        for option in permutations:
            board = GameBoard()
            board.play_move("X", option[0])
            board.play_move("X", option[1])
            ai = Hard("X", "O")
            assert_equal(option[2], ai.take_win(board))

def block_loss_if_available_in_row_test():
    for row in [[0, 1, 2], [3, 4, 5], [6, 7, 8]]:
        permutations = itertools.permutations(row)
        for option in permutations:
            board = GameBoard()
            board.play_move("O", option[0])
            board.play_move("O", option[1])
            ai = Hard("X", "O")
            assert_equal(option[2], ai.block_loss(board))
    
def block_loss_if_available_in_column_test():
    for column in [[0, 3, 6], [1, 4, 7], [2, 5, 8]]:
        permutations = itertools.permutations(column)
        for option in permutations:
            board = GameBoard()
            board.play_move("O", option[0])
            board.play_move("O", option[1])
            ai = Hard("X", "O")
            assert_equal(option[2], ai.block_loss(board))

def block_loss_if_available_in_diagonal_test():
    for diagonal in [[0, 4, 8], [2, 4, 6]]:
        permutations = itertools.permutations(diagonal)
        for option in permutations:
            board = GameBoard()
            board.play_move("O", option[0])
            board.play_move("O", option[1])
            ai = Hard("X", "O")
            assert_equal(option[2], ai.block_loss(board))

def should_play_in_opposite_corner_test():
    for corner in GameBoard().corner_positions:
        board = GameBoard()
        board.play_move("X", board.center_position)
        board.play_move("O", corner)
        ai = Hard("X", "O")
        assert_equal(True, ai.should_take_opposite_corner(board))

def should_take_opposite_corner_test():
    for corner in [[0, 8], [2, 6]]:
        permutations = itertools.permutations(corner)
        for option in permutations:
            board = GameBoard()
            board.play_move("O", option[0])
            board.play_move("X", 4)
            ai = Hard("X", "O")
            assert_equal(option[1], ai.take_opposite_corner(board))

def take_corner_if_available_test():
    for corner in GameBoard().corner_positions:
        board = GameBoard()
        board.play_move("X", corner)
        board.play_move("O", 4)
        ai = Hard("X", "O")
        move = ai.take_corner(board)
        result = move in GameBoard().corner_positions
        assert_equal(True, result)

def ensuree_take_edge_actually_takes_the_available_edge_test():
    permutations = itertools.permutations(GameBoard().edge_positions)
    for option in permutations:
        board = GameBoard()
        board.play_move("O", option[0])
        board.play_move("X", option[1])
        board.play_move("O", option[2])
        ai = Hard("X", "O")
        move = ai.take_edge(board)
        assert_equal(move, option[3])

def ai_plays_itself_and_draw_game_test():
    ai = Hard("X", "O")
    ai2 = Hard("O", "X")
    board = GameBoard()
    state = GameState(board)
    current_player = ai
    while state.has_winner() == False and GameState(board).is_draw() == False:
        move = current_player.make_move(board)
        board.play_move(current_player._symbol, move)
        if current_player == ai:
            current_player = ai2
        else:
            current_player = ai
    assert_equal(False, state.has_winner())
    assert_equal(True, state.is_draw())
    
def play_all_games():
    ai = Hard("X", "O")
    games = list(itertools.permutations(range(0, 9)))
    for game in games:
        board = GameBoard()
        state = GameState(board)
        play_fixed_moves(game, ai, board, state)
                
def ensure_fork_blocked_test():
    ai = Hard("X", "O")
    board = GameBoard()
    state = GameState(board)
    game = (0, 4, 6, 1, 3, 2, 5, 7, 8)
    play_fixed_moves(game, ai, board, state)
    
def play_fixed_moves(moves, ai_player, board, state):
    for move in moves:
        if board.positions[move] == "":
            print("Human play at {0}".format(move))
            board.play_move("O", move)
            if state.has_winner():
                # Human has won
                print("Uh oh.\nBoard: {0}\nMoves: {1}".format(board.positions, moves))
                assert False
            elif state.is_draw():
                # This is OK
                assert True
                break
            ai_move = ai_player.make_move(board)
            print("AI play at {0}".format(ai_move))
            board.play_move("X", ai_move)
            if state.has_winner():
                # AI has won
                assert True
                break
            elif state.is_draw():
                # This is OK
                assert True
                break
            
def ensure_second_fork_blocked_test():
    ai = Hard("X", "O")
    board = GameBoard()
    state = GameState(board)
    game = (5, 4, 7, 0, 8, 2, 1, 3, 6)
    play_fixed_moves(game, ai, board, state)
