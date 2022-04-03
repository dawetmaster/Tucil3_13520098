from puzzle import Puzzle
from puzzlenode import PuzzleNode
from collections import deque
import search
import time
import menu


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
    # assume logging is enabled
    log = "Solution:\n"
    while solution:
        node = solution.pop()
        print("Step " + str(step))
        log += "Step " + str(step) + "\n"
        node.print()
        log += node.get_printed_text()
        print()
        step += 1
    print("** End of solution **")
    log += "\n** End of solution **"
    return log


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
        # start calculating execution time
        start_time = time.time()
        solution, node_count = get_solution(base_tree)
        # end calculating execution time
        end_time = time.time()
        solution_log = print_solution(solution)
        print("Number of nodes (Simpul dibangkitkan): " + str(node_count))
        solution_log += "\nNumber of nodes (Simpul dibangkitkan): " + str(node_count)
        # print execution time
        print("Execution time: " + str(end_time - start_time) + " seconds")
        solution_log += "\nExecution time: " + str(end_time - start_time) + " seconds"
        # Enable logging prompt question
        print("Do you want to save the solution to a file? (Y/n)")
        while True:
            # get input
            input_str = input()
            # if input is Y or y
            if input_str.lower() == "y" or input_str.lower() == "":
                # insert file name dialog
                filename = menu.insert_file_name_dialog()
                # default file name is result.txt if filename is empty
                if filename == "":
                    filename = "result.txt"
                # write solution to file
                with open(filename, "w") as f:
                    f.write(solution_log)
                # print termination message
                print("Solution saved to " + filename)
                # break
                break
            # if input is n or N
            elif input_str.lower() == "n":
                # break
                break
            # if input is not Y or y or n or N
            else:
                # print error
                print("Error: invalid input")
        # reset static attribute node_count to zero
        PuzzleNode.node_count = 0
    else:
        print("Termination message:")
        print("This puzzle is not solvable")
