class GameBoard():
    def __init__(self):
        self._board = None
        self.reset()

    @property
    def positions(self):
        return self._board

    def play_move(self, player, position):
        if not self._is_position_valid(position):
            raise ValueError("{0} is not a valid board position".format(position))
        if not self._is_position_open(position):
            raise ValueError("{0} is already taken".format(position))
        
        self.positions[position] = player

    def _is_position_valid(self, position):
        return position >= 0 and position < len(self.positions)
        
    def _is_position_open(self, position):
        return self.positions[position] == ""

    def _row_check(self):
        return self.check_items(self._rows)
    
    @property
    def _rows(self):
        return list(map(self._row, list(range(3))))
    
    def _row(self, number):
        start_cell = number * 3
        return self.positions[start_cell:start_cell + 3] 

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
        return [[self.positions[i] for i in [0, 4, 8]], [self.positions[i] for i in [2, 4, 6]]]

    def reset(self):
        self._board = ["", "", "", "", "", "", "", "", ""]

