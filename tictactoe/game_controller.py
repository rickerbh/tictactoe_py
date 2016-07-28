from tictactoe.ai_player import AIPlayer
from tictactoe.game_board import GameBoard
from tictactoe.game_state import GameState
import random

class GameController():
    def __init__(self, symbol):
        self._board = GameBoard()
        self._player_symbol = symbol
        self._ai_player = AIPlayer(self._ai_symbol, symbol)

    def _ai_symbol(self):
        if self._player_symbol == "X":
            return "O"
        else:
            return "X"
        
    def make_ai_move(self):
        symbol = self._ai_symbol()
        position = self._ai_player.best_move(self._board)
        self._play(symbol, position)
