from tictactoe.ai_strategies.ai_strategy import AIStrategy
import random

class Easy(AIStrategy):
    def __init__(self, symbol, other_symbol):
        AIStrategy.__init__(self, symbol, other_symbol)

    def make_move(self, board):
        positions = dict(enumerate(board.positions))
        available_positions = [key for (key, value) in positions.items() if value == ""]
        return random.choice(available_positions)
