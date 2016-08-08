class AIStrategy():
    def __init__(self, symbol, other_symbol):
        self._symbol = symbol
        self._other_symbol = other_symbol

    def make_move(self, board):
        raise NotImplementedError
