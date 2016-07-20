from tictactoe.game_board import GameBoard

class GameController():
    def __init__(self, symbol):
        self._player_symbol = symbol

    def _ai_symbol(self):
        if self._player_symbol == "X":
            return "O"
        else:
            return "X"
        
