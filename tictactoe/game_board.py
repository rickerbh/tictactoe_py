class GameBoard():
    def __init__(self):
        self._board = None
        self.reset()

    @property
    def game_state(self):
        return self._board

    def play_move(self, player, position):
        if not self._is_position_valid(position):
            raise ValueError("{0} is not a valid board position".format(position))
        if not self._is_position_open(position):
            raise ValueError("{0} is already taken".format(position))
        if self.has_winner():
            raise ValueError("Game is over")
        
        self._board[position] = player

    def _is_position_valid(self, position):
        return position >= 0 and position < len(self.game_state)
        
    def _is_position_open(self, position):
        return self.game_state[position] == ""

    def has_winner(self):
        return any([self._row_check(), self._column_check(), self._diagonal_check()])

    def _row_check(self):
        return self.check_items(self._rows)
    
    @property
    def _rows(self):
        return list(map(self._row, list(range(3))))
    
    def _row(self, number):
        start_cell = number * 3
        return self._board[start_cell:start_cell + 3] 

    def check_items(self, items):
        checked_items = map(self._all_same, items)
        return any(checked_items)
    
    def _all_same(self, items):
        return len(set(items)) == 1 and not items[0] == ""

    def _column_check(self):
        return self.check_items(self._columns)
    
    @property
    def _columns(self):
        return list(map(self._column, list(range(3))))
    
    def _column(self, number):
        return [self._board[i] for i in [number, number + 3, number + 6]]

    def _diagonal_check(self):
        return self.check_items(self._diagonals)
    
    @property
    def _diagonals(self):
        return [[self._board[i] for i in [0, 4, 8]], [self._board[i] for i in [2, 4, 6]]]

    def reset(self):
        self._board = ["", "", "", "", "", "", "", "", ""]

    def is_draw(self):
        def is_not_empty(item):
            return not item == ""
        
        if self.has_winner():
            return False
        return len(list(filter(is_not_empty, self._board))) == len(self._board)
    
