from puzzle import Puzzle
from puzzlenode import PuzzleNode
from collections import deque
import search


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


def solvability_est_value(puzzle):
    # get solvable estimate from the puzzle
    return puzzle.get_solvable_estimate()


def print_count_smaller(puzzle):
    # print count of smaller values
    # assume the puzzle is a valid Puzzle class

    # do it traversally from tile number 1 to tile number 15
    for i in range(1, 16):
        # print the number of tiles whose number is smaller than i
        print("kurang(" + str(i) + "): "
              + str(puzzle.count_smaller(i)))


def get_solution(base_tree):
    # get solution from given puzzle node
    # return as stack of nodes

    # check if puzzle is already solved
    # if solved, generate solution with just the node
    # otherwise, generate solution with the node and its children
    if base_tree.puzzle.is_solved():
        return deque([base_tree])
    else:
        return search.get_solution_stack(base_tree)


def print_solution(solution):
    # assume given solution is a valid stack of nodes
    step = 0
    # print solution
    print("Solution:")
    while solution:
        node = solution.pop()
        print("Step " + str(step))
        node.print()
        print()
        step += 1
    print("** End of solution **")


def main(pz_array):
    # main process of pz_array solving
    # assume the pz_array is a valid numpy array

    # create base tree from pz_array
    base_tree = make_base_tree(pz_array)

    # print base tree
    print("Base tree:")
    base_tree.print()

    # print solvability message
    print_solvability_msg(base_tree.puzzle)

    # give space
    print()

    # for each tile number 1 to 15, print tile with smaller values
    print("Value of kurang(i) for each non-empty tile\n")
    print_count_smaller(base_tree.puzzle)

    # give space
    print()

    # print solvability estimate values
    print(
        "Estimate values (sum(kurang(i) + X)): "
        + str(solvability_est_value(base_tree.puzzle))
        )

    # print solvability message
    print_solvability_msg(base_tree.puzzle)

    # do searching process if puzzle is solvable
    # otherwise print termination message
    # then terminate the search process
    if check_solvable(base_tree.puzzle):
        solution = get_solution(base_tree)
        print_solution(solution)
    else:
        print("Termination message:")
        print("This puzzle is not solvable")
