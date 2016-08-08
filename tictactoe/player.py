class Player():
    def __init__(self, symbol):
        self._symbol = symbol
        
    def play_notification(self, game_controller):
        raise NotImplementedError

    @property
    def symbol(self):
        return self._symbol
