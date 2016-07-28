from collections import Counter
import random

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
            return self._make_opening_ai_move()
        elif moves == len(positions) - 1:
            return self._make_responding_ai_move(board)
        elif self.win_available(board):
            return self.take_win(board)
        elif self.loss_available(board):
            return self.block_loss(board);
        elif self.should_take_opposite_corner(board):
            return self.take_opposite_corner(board)
        elif self.corner_available(board):
            return self.take_corner(board)
        elif self.edge_available(board):
            return self.take_edge(board)

    def _make_opening_ai_move(self):
        return self._random_corner()
    
    def _random_corner(self):
        return random.choice([0, 2, 6, 8])
    
    def _make_responding_ai_move(self, board):
        if any(board.corners) or any(board.edges):
            return 4
        elif any(board.center):
            return self._random_corner()

    def win_available(self, board):
        winnables = board.rows + board.columns + board.diagonals
        return any(map(self.is_winnable, winnables))

    def is_winnable(self, items):
        return self.nearly_won_check(self._symbol, items)
    
    def nearly_won_check(self, symbol, items):
        freqs = Counter(items)
        return freqs[symbol] == 2 and freqs[""] == 1

    def take_win(self, board):
        offset = 0
        for items in board.rows:
            if self.is_winnable(items):
                return items.index("") + offset
            offset = offset + 3

        offset = 0
        for items in board.columns:
            if self.is_winnable(items):
                return items.index("") * 3 + offset
            offset = offset + 1

        diagonal = 0
        for items in board.diagonals:
            if self.is_winnable(items):
                if diagonal == 0:
                    return items.index("") * 4
                else:
                    return items.index("") * 2 + 2
            diagonal = 1

    def loss_available(self, board):
        loseables = board.rows + board.columns + board.diagonals
        return any(map(self.is_loseable, loseables))

    def is_loseable(self, items):
        return self.nearly_won_check(self._other_symbol, items)

    def block_loss(self, board):
        offset = 0
        for items in board.rows:
            if self.is_loseable(items):
                return items.index("") + offset
            offset = offset + 3

        offset = 0
        for items in board.columns:
            if self.is_loseable(items):
                return items.index("") * 3 + offset
            offset = offset + 1

        diagonal = 0
        for items in board.diagonals:
            if self.is_loseable(items):
                if diagonal == 0:
                    return items.index("") * 4
                else:
                    return items.index("") * 2 + 2
            diagonal = 1

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

    def corner_available(self, board):
        return "" in board.corners

    def take_corner(self, board):
        return board.corners.index("") * (board.corners.index("") + 1)

    def edge_available(self, board):
        return "" in board.edges

    def take_edge(self, board):
        return board.edges.index("") * 2 + 1
