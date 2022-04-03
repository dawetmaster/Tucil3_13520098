from puzzle import Puzzle
from puzzlenode import PuzzleNode


def make_base_puzzle(pz_array):
    # return new Puzzle class from a numpy array
    return Puzzle(pz_array)


def make_base_tree(pz_array):
    # return new PuzzleNode class from a numpy array
    return PuzzleNode(make_base_puzzle(pz_array))


def check_solvable(puzzle):
    # check if a Puzzle class is solvable
    # return True if solvable
    # return False otherwise
    # assume the puzzle is a valid Puzzle class

    # using method is_solvable()
    return puzzle.is_solvable()


def print_solvability_msg(puzzle):
    # print solvability message
    # assume the puzzle is a valid Puzzle class

    # using method get_solvable_message
    print("This puzzle is " + puzzle.get_solvable_message())


def main(pz_array):
    # main process of pz_array solving
    # assume the pz_array is a valid numpy array

    # create base tree from pz_array
    base_tree = make_base_tree(pz_array)

    # print base tree
    print("Base tree:")
    base_tree.print()

    # check if base tree is solvable
    if check_solvable(base_tree.puzzle):
        # print solvability message
        print_solvability_msg(base_tree.puzzle)
