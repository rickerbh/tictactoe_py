import importlib

class AIStrategyFactory():
    def __init__(self):
        pass

    def strategy(self, name, player_one_symbol, player_two_symbol):
        m = importlib.import_module("tictactoe.ai_strategies." + name.lower())
        MyStrategy = getattr(m, name)
        return MyStrategy(player_one_symbol, player_two_symbol)
