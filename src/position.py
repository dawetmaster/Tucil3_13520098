class Position:
    # DEFINITION
    "Base class for position"

    # attributes
    row = 0
    col = 0

    # constructors
    def __init__(self, row=0, col=0):
        "Constructor"

        self.row = row
        self.col = col

    # methods
    def get_row(self):
        "Returns row"

        return self.row

    def get_col(self):
        "Returns column"

        return self.col

    def set_row(self, row):
        "Sets row to row (int)"

        self.row = row

    def set_col(self, col):
        "Sets col to col (int)"

        self.col = col

    def is_row_valid(self, row_size):
        "Checks if position is valid in row"

        return self.row < row_size and self.row >= 0

    def is_col_valid(self, col_size):
        "Checks if position is valid in column"

        return self.col < col_size and self.col >= 0

    def is_out_of_bounds(self, row_size, col_size):
        "Checks if position is out of boundary"

        return not (self.is_row_valid(row_size) and self.is_col_valid(col_size))

    def is_top_most(self):
        "Checks if position is topmost"

        return self.row == 0

    def is_bottom_most(self, row_size):
        "Checks if position is bottommost"

        return self.row == row_size - 1

    def is_left_most(self):
        "Checks if position is leftmost"

        return self.col == 0

    def is_right_most(self, col_size):
        "Checks if position is rightmost"

        return self.col == col_size - 1
