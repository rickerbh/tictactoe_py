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
        return any([self._board._row_check(),
                    self._board._column_check(),
                    self._board._diagonal_check()])

