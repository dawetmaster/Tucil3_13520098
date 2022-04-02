# ATTENTION
# numpy is required for this file

import numpy as np
import position as pos
from moves import Moves

# CONSTANTS
BASE_ARRAY = np.array(
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ],
    dtype=np.int8
    )


class Puzzle:
    # DEFINITION
    "Base class for puzzle"

    # ATTRIBUTE
    # private puzzle: list of list of int
    # private steps: int
    # private last_move: enum Moves

    # CONSTRUCTORS
    def __init__(self, puzzle=BASE_ARRAY, steps=0, last_move=""):
        self.puzzle = puzzle
        self.steps = steps
        self.last_move = last_move

    # METHODS
    def get_puzzle(self):
        "Returns puzzle"

        return self.puzzle

    def get_steps(self):
        "Returns steps"

        return self.steps

    def get_last_move(self):
        "Returns last move"

        return self.last_move

    def clone(self):
        "Clones puzzle"

        return Puzzle(self.puzzle.copy(), self.steps, self.last_move)

    def to_array(self):
        "Converts puzzle to array"

        return self.puzzle.copy()

    def to_string(self):
        "Converts puzzle to string"

        return str(self.puzzle)

    def print(self):
        "Prints puzzle"

        result = ""
        for i in range(4):
            result += "+----+----+----+----+\n"
            for j in range(4):
                result += (
                    "|"
                    + (
                        "{:3d} ".format(self.puzzle[i][j])
                        if self.puzzle[i][j] != 16 else "    "
                        )
                    )
            result += "|\n"
        result += "+----+----+----+----+"
        print(result)

    def print_state(self):
        "Prints steps with last move"

        print("Steps: " + str(self.steps))
        print("Last move: " + str(self.last_move))

    def is_solved(self):
        "Checks if puzzle is solved"

        return np.array_equal(self.puzzle, BASE_ARRAY)

    def get_tile_position(self, number):
        "Returns position of tile"

        for i in range(4):
            for j in range(4):
                if self.puzzle[i][j] == number:
                    return pos.Position(i, j)
        raise ValueError("Tile not found")

    def get_tile_number(self, position):
        "Returns number of tile"

        return self.puzzle[position.get_row()][position.get_col()]

    def get_tile_position_16(self):
        "Returns position of tile 16"

        return self.get_tile_position(16)

    def swap_tile(self, pos1, pos2):
        "Swaps two tiles"

        temp = self.puzzle[pos1.get_row()][pos1.get_col()]
        self.puzzle[pos1.get_row()][pos1.get_col()] = self.puzzle[pos2.get_row()][pos2.get_col()]
        self.puzzle[pos2.get_row()][pos2.get_col()] = temp

    def move_up(self):
        "Moves tile up"

        pos1 = self.get_tile_position(16)
        pos2 = pos.Position(pos1.get_row() - 1, pos1.get_col())
        self.swap_tile(pos1, pos2)
        self.steps += 1
        self.last_move = Moves.UP

    def move_down(self):
        "Moves tile down"

        pos1 = self.get_tile_position(16)
        pos2 = pos.Position(pos1.get_row() + 1, pos1.get_col())
        self.swap_tile(pos1, pos2)
        self.steps += 1
        self.last_move = Moves.DOWN

    def move_left(self):
        "Moves tile left"

        pos1 = self.get_tile_position(16)
        pos2 = pos.Position(pos1.get_row(), pos1.get_col() - 1)
        self.swap_tile(pos1, pos2)
        self.steps += 1
        self.last_move = Moves.LEFT

    def move_right(self):
        "Moves tile right"

        pos1 = self.get_tile_position(16)
        pos2 = pos.Position(pos1.get_row(), pos1.get_col() + 1)
        self.swap_tile(pos1, pos2)
        self.steps += 1
        self.last_move = Moves.RIGHT

    # function count_all_smaller is defined
    # as how many tiles with smaller value than itself
    # that placed after itself
    def count_all_smaller(self, number):
        "Counts all tiles with smaller value than itself"

        count = 0
        # treat puzzle as one long array
        puzzle_array = self.puzzle.flatten()
        # get position of tile that contains specified number
        pos = puzzle_array.tolist().index(number)
        # from that position to the end of array
        # count how many tiles with smaller value than itself
        for i in range(pos, len(puzzle_array)):
            if puzzle_array[i] < number:
                count += 1
        return count

    # then, apply it to all 16 tiles in the puzzle
    # based on function count_all_smaller
    def get_count_all_smaller(self):
        "Counts all tiles with smaller value than itself"

        count = 0
        for i in range(1, 16):
            count += self.count_all_smaller(i)
        return count
    
    # tile with number 16 also have impact of heuristic cost
    # so, we need to calculate value of position of tile 16
    # tile 16 position is defined by (row, col)
    # return 1 if (row + col) is odd, otherwise 0
    def get_tile_16_heuristic_cost(self):
        "Returns heuristic cost of tile 16"

        pos = self.get_tile_position(16)
        return 1 if (pos.get_row() + pos.get_col()) % 2 == 1 else 0

    # then, we need to calculate heuristic cost of puzzle
    # by summing up heuristic cost of all tiles
    def get_heuristic_cost(self):
        "Returns heuristic cost of puzzle"

        return self.get_count_all_smaller() + self.get_tile_16_heuristic_cost()