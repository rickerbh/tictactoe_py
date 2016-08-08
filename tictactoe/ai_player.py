import functools
import random
from tictactoe.ai_strategies.hard import Hard
from tictactoe.player import Player

class AIPlayer(Player):
    def __init__(self, symbol, other_symbol):
        self._symbol = symbol
        self._other_symbol = other_symbol
        self._strategy = Hard(symbol, other_symbol)

    def play_notification(self, game_controller):
        game_controller.place_move(self, self._strategy.make_move(game_controller._board))
        
