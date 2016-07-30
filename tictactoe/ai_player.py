import functools
import random
from tictactoe.game_state import GameState

class AIPlayer():
    def __init__(self, symbol, other_symbol):
        self._symbol = symbol
        self._other_symbol = other_symbol

    def best_move(self, board):
        def is_empty(item): # TODO: Refactor as this is duplicated in game_board and game_controller_tests
            return item == ""

        positions = board.positions
        moves = len(list(filter(is_empty, positions)))
        
        if moves == len(positions):
            return self._make_opening_ai_move(board)
        elif moves == len(positions) - 1:
            return self._make_responding_ai_move(board)
        elif board.win_available(self._symbol):
            return self.take_win(board)
        elif board.win_available(self._other_symbol):
            return self.block_loss(board);
        elif self.should_take_opposite_corner(board):
            return self.take_opposite_corner(board)
        elif state.corner_available(board):
            return self.take_corner(board)
        elif state.edge_available(board):
            return self.take_edge(board)

    def _make_opening_ai_move(self, board):
        return board.random_corner
    
    def _make_responding_ai_move(self, board):
        if any(board.corners) or any(board.edges):
            return 4
        elif any(board.center):
            return board.random_corner

    def take_win(self, board):
        is_winnable = functools.partial(GameState(board).is_winnable, self._symbol)
        return self.complete_row(board, is_winnable)
        
    def complete_row(self, board, take_determinator):
        offset = 0
        for items in board.rows:
            if take_determinator(items):
                return items.index("") + offset
            offset = offset + 3

        offset = 0
        for items in board.columns:
            if take_determinator(items):
                return items.index("") * 3 + offset
            offset = offset + 1

        diagonal = 0
        for items in board.diagonals:
            if take_determinator(items):
                if diagonal == 0:
                    return items.index("") * 4
                else:
                    return items.index("") * 2 + 2
            diagonal = 1       
    
    def block_loss(self, board):
        is_loseable = functools.partial(GameState(board).is_winnable, self._other_symbol)
        return self.complete_row(board, is_loseable)

    def should_take_opposite_corner(self, board):
        for items in board.diagonals:
            if items[0] == self._other_symbol and items[2] == "" or items[2] == self._other_symbol == items[0] == "":
                return True
        return False

    def take_opposite_corner(self, board):
        diagonal = 0
        for items in board.diagonals:
            if items[0] == self._other_symbol and items[2] == "":
                if diagonal == 0:
                    return 8
                else:
                    return 6
            elif items[2] == self._other_symbol and items[0] == "":
                if diagonal == 1:
                    return 0
                else:
                    return 2
            diagonal = 1

    def take_corner(self, board):
        return board.corners.index("") * (board.corners.index("") + 1)

    def take_edge(self, board):
        return board.edges.index("") * 2 + 1
