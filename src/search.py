from puzzlenode import PuzzleNode
from puzzleprioqueue import PuzzlePrioQueue
from collections import deque


def get_solution_stack(base_tree):
    # assume base_tree is valid PuzzleNode class
    # base_tree puzzle is also not solved
    # return solution stack

    # method:
    # 1. create a priority queue
    # 2. add base_tree to the queue
    # 3. while queue is not empty:
    # 4.   poll the first node from the queue
    # 5.   if the node is solved:
    # 6.       return the solution stack
    # 7.   else:
    # 8.       add the children of the node to the queue
    # 9. return None

    # 1. create a priority queue
    # 2. add base_tree to the queue
    queue = PuzzlePrioQueue()
    queue.add(base_tree)

    node_count = 1

    # 3. while queue is not empty:
    while not queue.is_empty():
        # 4.   poll the first node from the queue
        node = queue.poll()

        # node is a valid PuzzleNode object

        # 5.   if the node is solved:
        if node.puzzle.is_solved():
            # 6a. create solution stack
            solution_stack = deque()

            # 6b. add node to solution stack
            solution_stack.append(node)

            # 6c. while node is not base_tree:
            while node.parent is not None:
                # 6d. add node's parent to solution stack
                solution_stack.append(node.parent)

                # 6e. set node to node's parent
                node = node.parent

            # 6f. return solution stack
            return solution_stack, node_count

        # 7.   else:
        else:
            # 8a. get tile 16 position
            tile_16_pos = node.puzzle.get_tile_position_16()

            # 8b. add only valid moves to children
            if not tile_16_pos.is_left_most():
                # 8c. create child puzzle
                child_puzzle = node.puzzle.clone()
                child_puzzle.move_left()

                # 8d. create child node
                child_node = PuzzleNode(child_puzzle, node, [])

                # 8e. add child node to children
                node.add_child(child_node)

                # 8f. enqueue child node
                queue.add(child_node)

                node_count += 1

            # 8g. repeat for right, up, and down
            if not tile_16_pos.is_right_most(4):
                child_puzzle = node.puzzle.clone()
                child_puzzle.move_right()

                child_node = PuzzleNode(child_puzzle, node, [])
                node.add_child(child_node)

                queue.add(child_node)
                node_count += 1

            if not tile_16_pos.is_top_most():
                child_puzzle = node.puzzle.clone()
                child_puzzle.move_up()

                child_node = PuzzleNode(child_puzzle, node, [])
                node.add_child(child_node)

                queue.add(child_node)
                node_count += 1

            if not tile_16_pos.is_bottom_most(4):
                child_puzzle = node.puzzle.clone()
                child_puzzle.move_down()

                child_node = PuzzleNode(child_puzzle, node, [])
                node.add_child(child_node)

                queue.add(child_node)
                node_count += 1

        # endif
    # end while
