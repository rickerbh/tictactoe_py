class BoardStringification():

    def print_game_positions(self, board):
        formatted_rows = map(self.print_row, board.rows)
        return self.print_spacer().join(formatted_rows)

    def print_row(self, row):
        normalised_row = [" " if x == "" else x for x in row]
        return " {0} | {1} | {2}\n".format(normalised_row[0], normalised_row[1], normalised_row[2])

    def print_spacer(self):
        return "---+---+---\n"
