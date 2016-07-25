from tictactoe.game_board import GameBoard

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
        return self.check_items(self._board._rows)
    
    def check_items(self, items):
        checked_items = map(self._all_same, items)
        return any(checked_items)
    
    def _all_same(self, items):
        return len(set(items)) == 1 and not items[0] == ""

    def _column_check(self):
        return self.check_items(self._board._columns)
    
    def _diagonal_check(self):
        return self.check_items(self._board._diagonals)
    
