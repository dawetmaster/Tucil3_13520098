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

    def count_smaller(self, number):
        """
        Returns number of tiles whose number is smaller than given number
        that placed after the tile with the given number
        """

        count = 0
        # flatten the whole puzzle
        flat_puzzle = self.puzzle.flatten()
        # get tile position that have the given number
        pos = 0
        while flat_puzzle[pos] != number:
            pos += 1
        # count the number of tiles whose number is smaller than given number
        # that placed after tile with the given number
        for i in range(pos + 1, len(flat_puzzle)):
            if flat_puzzle[i] < number:
                count += 1

        return count

    # function count_all_smaller
    # returns number of tiles whose number is smaller than given number
    # process is done traversally from first element to last element
    # complexity is O(n**2)
    def count_all_smaller(self):
        # flatten the whole puzzle
        flat_puzzle = self.puzzle.flatten()
        # for each pass, get tile number from current element
        # and count number of tiles whose number is smaller than it
        # that placed after the current element
        count = 0
        for i in range(len(flat_puzzle)):
            for j in range(i + 1, len(flat_puzzle)):
                if flat_puzzle[i] > flat_puzzle[j]:
                    count += 1
        return count

    # function tile_16_estimate
    # returns (row + col) mod 2 of tile numbered 16
    # just get the position of tile numbered 16
    def tile_16_estimate(self):
        pos_16 = self.get_tile_position(16)
        return (pos_16.get_row() + pos_16.get_col()) % 2

    def get_solvable_estimate(self):
        "Returns solvable estimate"

        return self.count_all_smaller() + self.tile_16_estimate()

    def is_solvable(self):
        "Checks if puzzle is solvable"

        return self.get_solvable_estimate() % 2 == 0

    def get_solvable_message(self):
        "Returns solvable message"

        if self.is_solvable():
            return "Solvable"
        else:
            return "Not solvable"

    # Heuristic cost is defined of how many tiles displaced from goal state
    def get_heuristic_cost(self):
        "Returns heuristic cost"

        count = 0
        flat_puzzle = self.puzzle.flatten()
        for i in range(len(flat_puzzle)):
            if flat_puzzle[i] != BASE_ARRAY.flatten()[i]:
                count += 1
        return count

    def get_total_cost(self):
        return self.steps + self.get_heuristic_cost()
