from tictactoe.ai_strategies.ai_strategy import AIStrategy
from tictactoe.game_state import GameState
import functools

class Hard(AIStrategy):
    def __init__(self, symbol, other_symbol):
        AIStrategy.__init__(self, symbol, other_symbol)
        
    def make_move(self, board):
        def is_empty(item):
            return item == ""

        positions = board.positions
        moves = len(list(filter(is_empty, positions)))
        state = GameState(board)
        
        if moves == len(positions):
            return self._make_opening_ai_move(board)
        elif moves == len(positions) - 1:
            return self._make_responding_ai_move(board)
        elif state.win_available(self._symbol):
            return self.take_win(board)
        elif state.win_available(self._other_symbol):
            return self.block_loss(board)
        elif moves == len(positions) - 3 and state.block_opposite_fork_opportunity(self._symbol):
            return self.take_edge(board)
        elif moves == len(positions) - 3 and state.block_corner_fork_opportunity(self._symbol):
            return self.take_corner_fork_block(self._symbol, board)
        elif self.should_take_opposite_corner(board):
            return self.take_opposite_corner(board)
        elif state.corner_available():
            return self.take_corner(board)
        elif state.edge_available():
            return self.take_edge(board)

    def _make_opening_ai_move(self, board):
        return board.random_corner
    
    def _make_responding_ai_move(self, board):
        if any(board.corners) or any(board.edges):
            return board.center_position
        elif any(board.center):
            return board.random_corner

    def take_win(self, board):
        is_winnable = functools.partial(GameState(board).is_winnable, self._symbol)
        return self.complete_row(board, is_winnable)
    
    def complete_row(self, board, take_determinator):
        offset = 0
        for items in board.rows:
            if take_determinator(items):
                return items.index("") + offset
            offset = offset + 3

        offset = 0
        for items in board.columns:
            if take_determinator(items):
                return items.index("") * 3 + offset
            offset = offset + 1

        diagonal = 0
        for items in board.diagonals:
            if take_determinator(items):
                if diagonal == 0:
                    return items.index("") * 4
                else:
                    return items.index("") * 2 + 2
            diagonal = 1       
                
    def block_loss(self, board):
        is_loseable = functools.partial(GameState(board).is_winnable, self._other_symbol)
        return self.complete_row(board, is_loseable)

    def should_take_opposite_corner(self, board):
        for items in board.diagonals:
            if items[0] == self._other_symbol and items[2] == "" or items[2] == self._other_symbol and items[0] == "":
                return True
        return False

    def take_opposite_corner(self, board):
        diagonal = 0
        result_mapping = {0: [8, 0], 1: [6, 2]}
        for items in board.diagonals:
            option = diagonal
            if items[0] == self._other_symbol and items[2] == "":
                return result_mapping[option][0]
            elif items[2] == self._other_symbol and items[0] == "":
                return result_mapping[option][1]
            diagonal = 1

    def take_corner(self, board):
        return {0: 0, 1: 2, 2: 6, 3: 8}[board.corners.index("")]

    def take_edge(self, board):
        return board.edges.index("") * 2 + 1

    def take_corner_fork_block(self, symbol, board):
        edges = board.edges
        blocking_moves = {0: (0, 1), 2: (0, 2), 6: (1, 3), 8: (2, 3)}

        def is_other_symbol(position):
            return position != "" and position != symbol

        def find_fork(pair):
            first = pair[0]
            second = pair[1]
            return is_other_symbol(edges[first]) and is_other_symbol(edges[second])

        for move in blocking_moves:
            if find_fork(blocking_moves[move]):
                return move
