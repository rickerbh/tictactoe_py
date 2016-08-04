from tictactoe.ai_player import AIPlayer
from tictactoe.game_board import GameBoard
from tictactoe.game_state import GameState
import random
from collections import Counter

class GameController():
    def __init__(self, player_a, player_b, won_notification, draw_notification):
        self._board = GameBoard()
        self._player_a = player_a
        self._player_b = player_b
        self._won = won_notification
        self._draw = draw_notification

    def notify_play(self):
        freqs = Counter(self._board.positions)
        if freqs[self._player_a.symbol] <= freqs[self._player_b.symbol]:
            self._player_a.play_notification(self)
        else:
            self._player_b.play_notification(self)
    
    def place_move(self, player, position):
        self._board.play_move(player.symbol, position)
        try:
            self._check_game_state()
        except Exception as e:
            if e.args[0] == "Draw":
                self._draw()
            elif e.args[0] == "Won":
                self._won()
            else:
                raise e
        else:
            self.notify_play()
            
    def _check_game_state(self):
        state = GameState(self._board)
        if state.is_draw():
            raise Exception("Draw")
        elif state.has_winner():
            raise Exception("Won")

    def reset(self):
        self._board.reset()
            
