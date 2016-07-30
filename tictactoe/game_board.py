import random

class GameBoard():
    def __init__(self):
        self._board = None
        self.reset()

    @property
    def positions(self):
        return self._board

    def play_move(self, symbol, position):
        if not self._is_position_valid(position):
            raise ValueError("{0} is not a valid board position".format(position))
        if not self._is_position_open(position):
            raise ValueError("{0} is already taken".format(position))
        
        self.positions[position] = symbol

    def _is_position_valid(self, position):
        return position >= 0 and position < len(self.positions)
        
    def _is_position_open(self, position):
        return self.positions[position] == ""

    @property
    def rows(self):
        return list(map(self._row, list(range(3))))
    
    def _row(self, number):
        start_cell = number * 3
        return self.positions[start_cell:start_cell + 3] 

    @property
    def columns(self):
        return list(map(self._column, list(range(3))))

    def _column(self, number):
        return self._get_cells([number, number + 3, number + 6])

    def _get_cells(self, cells):
        return [self.positions[i] for i in cells]
    
    @property
    def diagonals(self):
        return [self._get_cells([0, 4, 8]), self._get_cells([2, 4, 6])]

    def reset(self):
        self._board = ["", "", "", "", "", "", "", "", ""]

    @property
    def edges(self):
        return self._get_cells([1, 3, 5, 7])

    @property
    def corners(self):
        return self._get_cells(self.corner_positions)

    @property
    def center(self):
        return self._get_cells([4])

    @property
    def center_position(self):
        return 4

    @property
    def corner_positions(self):
        return [0, 2, 6, 8]

    @property
    def all_winnables(self):
        return self.rows + self.columns + self.diagonals

    @property
    def random_corner(self):
        return random.choice(self.corner_positions)
    
