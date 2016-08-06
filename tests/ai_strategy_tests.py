from nose.tools import *
from tictactoe.ai_strategy import AIStrategy
from tictactoe.game_board import GameBoard
from tictactoe.game_state import GameState
import functools
import itertools

def ai_strategy_makes_best_opening_move_test():
    ai = AIStrategy("X", "O")
    move = ai.make_move(GameBoard())
    result = move in GameBoard().corner_positions
    assert_equal(True, result)

def _o_finder(accum, item):
    if (accum):
        return accum
    return item == "O"

def ai_strategy_responds_to_opening_corner_test():
    for move in GameBoard().corner_positions:
        board = GameBoard()
        board.play_move("X", move)
        ai = AIStrategy("O", "X")
        result = ai.make_move(board)
        assert_equal(4, result)
    
def ai_strategy_responds_to_opening_edge_test():
    for move in GameBoard().edge_positions:
        board = GameBoard()
        board.play_move("X", move)
        ai = AIStrategy("O", "X")
        result = ai.make_move(board)
        assert_equal(board.center_position, result)

def ai_strategy_responds_to_opening_center_test():
    board = GameBoard()
    board.play_move("X", board.center_position)
    ai = AIStrategy("O", "X")
    result = ai._make_responding_ai_move(board)
    assert_equal(True, result in board.corner_positions)
    
def ai_strategy_takes_win_if_available_in_row_test():
    for row in [[0, 1, 2], [3, 4, 5], [6, 7, 8]]:
        permutations = itertools.permutations(row)
        for option in permutations:
            board = GameBoard()
            board.play_move("X", option[0])
            board.play_move("X", option[1])
            ai = AIStrategy("X", "O")
            assert_equal(option[2], ai.take_win(board))
    
def ai_strategy_takes_win_if_available_in_column_test():
    for column in [[0, 3, 6], [1, 4, 7], [2, 5, 8]]:
        permutations = itertools.permutations(column)
        for option in permutations:
            board = GameBoard()
            board.play_move("X", option[0])
            board.play_move("X", option[1])
            ai = AIStrategy("X", "O")
            assert_equal(option[2], ai.take_win(board))

def ai_strategy_takes_win_if_available_in_diagonal_test():
    for diagonal in [[0, 4, 8], [2, 4, 6]]:
        permutations = itertools.permutations(diagonal)
        for option in permutations:
            board = GameBoard()
            board.play_move("X", option[0])
            board.play_move("X", option[1])
            ai = AIStrategy("X", "O")
            assert_equal(option[2], ai.take_win(board))

def ai_strategy_block_loss_if_available_in_row_test():
    for row in [[0, 1, 2], [3, 4, 5], [6, 7, 8]]:
        permutations = itertools.permutations(row)
        for option in permutations:
            board = GameBoard()
            board.play_move("O", option[0])
            board.play_move("O", option[1])
            ai = AIStrategy("X", "O")
            assert_equal(option[2], ai.block_loss(board))
    
def ai_strategy_block_loss_if_available_in_column_test():
    for column in [[0, 3, 6], [1, 4, 7], [2, 5, 8]]:
        permutations = itertools.permutations(column)
        for option in permutations:
            board = GameBoard()
            board.play_move("O", option[0])
            board.play_move("O", option[1])
            ai = AIStrategy("X", "O")
            assert_equal(option[2], ai.block_loss(board))

def ai_strategy_block_loss_if_available_in_diagonal_test():
    for diagonal in [[0, 4, 8], [2, 4, 6]]:
        permutations = itertools.permutations(diagonal)
        for option in permutations:
            board = GameBoard()
            board.play_move("O", option[0])
            board.play_move("O", option[1])
            ai = AIStrategy("X", "O")
            assert_equal(option[2], ai.block_loss(board))

def ai_strategy_should_play_in_opposite_corner_test():
    for corner in GameBoard().corner_positions:
        board = GameBoard()
        board.play_move("X", board.center_position)
        board.play_move("O", corner)
        ai = AIStrategy("X", "O")
        print("Placed in {0}".format(corner))
        assert_equal(True, ai.should_take_opposite_corner(board))

def ai_strategy_should_take_opposite_corner_test():
    for corner in [[0, 8], [2, 6]]:
        permutations = itertools.permutations(corner)
        for option in permutations:
            board = GameBoard()
            board.play_move("O", option[0])
            board.play_move("X", 4)
            ai = AIStrategy("X", "O")
            assert_equal(option[1], ai.take_opposite_corner(board))

def ai_strategy_take_corner_test():
    for corner in GameBoard().corner_positions:
        board = GameBoard()
        board.play_move("X", corner)
        board.play_move("O", 4)
        ai = AIStrategy("X", "O")
        move = ai.take_corner(board)
        result = move in GameBoard().corner_positions
        assert_equal(True, result)

def ai_strategy_take_edge_test():
    permutations = itertools.permutations(GameBoard().edge_positions)
    for option in permutations:
        board = GameBoard()
        board.play_move("O", option[0])
        board.play_move("X", option[1])
        board.play_move("O", option[2])
        ai = AIStrategy("X", "O")
        move = ai.take_edge(board)
        assert_equal(move, option[3])

def ai_strategy_play_aginst_itself_test():
    ai = AIStrategy("X", "O")
    ai2 = AIStrategy("O", "X")
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
    
def ai_strategy_play_all_games():
    ai = AIStrategy("X", "O")
    games = list(itertools.permutations(range(0, 9)))
    for game in games:
        board = GameBoard()
        state = GameState(board)
        for move in game:
            if board.positions[move] == "":
                board.play_move("O", move)
                if state.has_winner():
                    # Human has won
                    print("Uh oh.\nBoard: {0}\nMoves: {1}".format(board.positions, game))
                    assert False
                elif state.is_draw():
                    # This is OK
                    assert True
                    break
                board.play_move("X", ai.make_move(board))
                if state.has_winner():
                    # AI has won
                    assert True
                    break
                elif state.is_draw():
                    # This is OK
                    assert True
                    break
                
def ai_strategy_play_all_fail1_test():
    ai = AIStrategy("X", "O")
    board = GameBoard()
    state = GameState(board)
    game = (0, 4, 6, 1, 3, 2, 5, 7, 8)
    for move in game:
        if board.positions[move] == "":
            print("Human play at {0}".format(move))
            board.play_move("O", move)
            if state.has_winner():
                # Human has won
                print("Uh oh.\nBoard: {0}\nMoves: {1}".format(board.positions, game))
                assert False
            elif state.is_draw():
                # This is OK
                assert True
                break
            ai_move = ai.make_move(board)
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

def ai_strategy_play_all_fail2_test():
    ai = AIStrategy("X", "O")
    board = GameBoard()
    state = GameState(board)
    game = (5, 4, 7, 0, 8, 2, 1, 3, 6)
    for move in game:
        if board.positions[move] == "":
            print("Human play at {0}".format(move))
            board.play_move("O", move)
            if state.has_winner():
                # Human has won
                print("Uh oh.\nBoard: {0}\nMoves: {1}".format(board.positions, game))
                assert False
            elif state.is_draw():
                # This is OK
                assert True
                break
            ai_move = ai.make_move(board)
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
