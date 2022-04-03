from puzzle import Puzzle


class PuzzleNode:
    # DEFINITION
    "Tree data structure for puzzle"

    # ATTRIBUTES
    # private puzzle: Puzzle
    # private parent: PuzzleNode
    # private children: list of PuzzleNode

    # CONSTRUCTORS
    def __init__(self, puzzle=Puzzle(), parent=None, children=[]):
        self.puzzle = puzzle
        self.parent = parent
        self.children = children

    # METHODS
    def get_puzzle(self):
        "Returns puzzle"

        return self.puzzle

    def get_parent(self):
        "Returns parent"

        return self.parent

    def get_children(self):
        "Returns children"

        return self.children

    def set_parent(self, parent):
        "Sets parent"

        self.parent = parent

    def add_child(self, child):
        "Adds child"

        self.children.append(child)
        child.set_parent(self)

    def print(self):
        "Prints puzzle"

        self.puzzle.print()
        print("Parent: " + str(self.parent))
        print("Children: " + str(self.children))
        print("Last move: " + str(self.puzzle.get_last_move()))

    def get_printed_text(self):
        "Returns printed text"

        return (
            self.puzzle.get_printed_text()
            + "\nParent: "
            + str(self.parent)
            + "\nChildren: "
            + str(self.children)
            + "\nLast move: "
            + str(self.puzzle.get_last_move())
            )
