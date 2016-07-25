import random

class AIPlayer():
    def __init__(self, symbol):
        self._symbol = symbol

    def best_move(self, board):
        def is_empty(item): # TODO: Refactor as this is duplicated in game_board and game_controller_tests
            return item == ""

        positions = board.positions
        moves = len(list(filter(is_empty, positions)))
        if moves == len(positions):
            return self._make_opening_ai_move()
        elif moves == len(positions) - 1:
            return self._make_responding_ai_move(board)

    def _make_opening_ai_move(self):
        return self._random_corner()
    
    def _random_corner(self):
        return random.choice([0, 2, 6, 8])
    
    def _make_responding_ai_move(self, board):
        if any(board.corners) or any(board.edges):
            return 4
        elif any(board.center):
            return self._random_corner()

