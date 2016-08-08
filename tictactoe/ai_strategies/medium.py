from tictactoe.ai_strategies.ai_strategy import AIStrategy
from tictactoe.ai_strategies.easy import Easy
from tictactoe.ai_strategies.hard import Hard
import random

class Medium(AIStrategy):
    def __init__(self, symbol, other_symbol):
        AIStrategy.__init__(self, symbol, other_symbol)
        self._easy = Easy(self._symbol, self._other_symbol)
        self._hard = Hard(self._symbol, self._other_symbol)

    def make_move(self, board):
        move = None
        if random.randint(0, 4) % 4 == 0:
            return self._easy.make_move(board)
        return self._hard.make_move(board)
    
