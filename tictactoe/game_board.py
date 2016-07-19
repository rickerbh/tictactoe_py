class GameBoard():
    def __init__(self):
        self._board = ["", "", "", "", "", "", "", "", ""]

    @property
    def game_state(self):
        return self._board

    def play_move(self, player, position):
        if not self._is_position_valid(position):
            raise ValueError("{0} is not a valid board position".format(position))
        if not self._is_position_open(position):
            raise ValueError("{0} is already taken".format(position))

        self._board[position] = player

    def _is_position_valid(self, position):
        return position >= 0 and position < len(self.game_state)
        
    def _is_position_open(self, position):
        return self.game_state[position] == ""
    
 
