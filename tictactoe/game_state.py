from tictactoe.game_board import GameBoard
from collections import Counter
import functools

class GameState():
    def __init__(self, board):
        self._board = board

    def is_draw(self):
        def is_not_empty(item):
            return not item == ""
        
        if self.has_winner():
            return False
        return len(list(filter(is_not_empty, self._board.positions))) == len(self._board.positions)
    
    def has_winner(self):
        return any([self._row_check(),
                    self._column_check(),
                    self._diagonal_check()])

    def _row_check(self):
        return self.check_items(self._board.rows)
    
    def check_items(self, items):
        checked_items = map(self._all_same, items)
        return any(checked_items)
    
    def _all_same(self, items):
        return len(set(items)) == 1 and not items[0] == ""

    def _column_check(self):
        return self.check_items(self._board.columns)
    
    def _diagonal_check(self):
        return self.check_items(self._board.diagonals)

    def corner_available(self):
        return "" in self._board.corners

    def edge_available(self):
        return "" in self._board.edges

    def nearly_won_check(self, symbol, items):
        freqs = Counter(items)
        return freqs[symbol] == 2 and freqs[""] == 1

    def win_available(self, symbol):
        winnables = self._board.all_winnables
        win_determinator = functools.partial(self.is_winnable, symbol)
        return any(map(win_determinator, winnables))

    def is_winnable(self, symbol, items):
        return self.nearly_won_check(symbol, items)
    
