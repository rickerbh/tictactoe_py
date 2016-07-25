import random

class AIPlayer():
    def __init__(self):
        pass

    def best_move(self, state):
        def is_empty(item): # TODO: Refactor as this is duplicated in game_board and game_controller_tests
            return item == ""

        moves = len(list(filter(is_empty, state)))
        if moves == len(state):
            return self._make_opening_ai_move()

    def _make_opening_ai_move(self):
        return random.choice([0, 2, 6, 8])
        # random in 1-4. Take number, multiply it by

    # have a responding ai move. Need to determine if it should go in corner or center.

    # then, have a function that determines if there is an opportunity for the player (or AI) to win, and take it.

    # All these should be in an external class
