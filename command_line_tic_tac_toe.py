#!/usr/bin/env python3

import cmd
from tictactoe.ai_player import AIPlayer
from tictactoe.human_player import HumanPlayer
from tictactoe.game_controller import GameController
from tictactoe.board_stringification import BoardStringification

class CommandLineTicTacToe(cmd.Cmd):
    def __init__(self,
                 intro="Tic Tac Toe CLI. Type help for help.\n\nHuman. You are X. Good luck. Your move\n\n",
                 prompt="→ "):
        cmd.Cmd.__init__(self)
        self.intro = intro
        self.prompt = prompt
        self._human = HumanPlayer("X", self._notify_move)
        self._ai = AIPlayer("O", "X")
        self._controller = GameController(self._human, self._ai, self._won_notification, self._draw_notification)

    def _won_notification(self):
        print("Game over. It was won\n\n")
        self._print_board()
        self.do_reset(None)

    def _draw_notification(self):
        print("Game over. It was a draw\n\n")
        self._print_board()
        self.do_reset(None)
        
    def do_end(self, args):
        return True

    def help_end(self):
        print("End session")

    do_EOF = do_end

    help_EOF = help_end

    def do_reset(self, args):
        self.do_human_start(None)

    def help_reset(self):
        print("Reset the current game")

    def do_move(self, args):
        print("Move passed in is: {0}".format(args))
        try:
            self._controller.place_move(self._human, int(args))
        except ValueError as e:
            print("Sorry, can't make that move: {0}".format(e.args[0]))
        

    def help_move(self):
        print("move x: Make a move at position x on the board")

    def do_show_board(self, args):
        print("Current game state\n")
        self._print_board()

    def help_show_board(self):
        print("Shows the current state of the game")

    def do_ai_start(self, args):
        self._controller = GameController(self._ai, self._human, self._won_notification, self._draw_notification)
        self._controller.notify_play()

    def help_ai_start(self):
        print("Initiate a new game where the AI starts")

    def do_human_start(self, args):
       self._controller = GameController(self._human, self._ai, self._won_notification, self._draw_notification)
       self._controller.notify_play()

    def help_human_start(self):
        print("Initiate a new game where the AI starts")
        
    def _notify_move(self):
        print("Human, your move:\n")
        self._print_board()
        
    def _print_board(self):
        print(BoardStringification().print_game_positions(self._controller._board))
        
if __name__ == '__main__':
    cli = CommandLineTicTacToe()
    cli.cmdloop()
