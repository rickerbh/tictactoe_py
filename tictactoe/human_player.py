from tictactoe.player import Player

class HumanPlayer(Player):
    def __init__(self, symbol, writer):
        self._symbol = symbol
        self._writer = writer
        
    def play_notification(self, game_controller):
        self._writer()

