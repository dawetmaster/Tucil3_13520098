# from puzzle import Puzzle
from puzzlecomparator import compare


class PuzzlePrioQueue():
    # DEFINITION
    "Priority queue for puzzle"

    # ATTRIBUTES
    # private queue: list of PuzzleNode

    # CONSTRUCTORS
    def __init__(self):
        self.queue = []

    # METHODS

    # add puzzle with priority
    # puzzle with smaller cost goes in the 1st priority
    def add(self, puzzlenode):
        "Adds puzzle to queue"

        pz_idx = len(self.queue)
        self.queue.append(puzzlenode)
        while (
            pz_idx > 0
            and (
                compare(self.queue[pz_idx], self.queue[pz_idx - 1]) < 0
                )
                ):
            temp = self.queue[pz_idx - 1]
            self.queue[pz_idx - 1] = self.queue[pz_idx]
            self.queue[pz_idx] = temp
            pz_idx -= 1

    def clear(self):
        "Clears queue"

        self.queue = []

    def contains(self, puzzlenode):
        "Returns true if queue contains puzzle"

        return puzzlenode in self.queue

    def peek(self):
        "Returns first puzzle in queue"

        return self.queue[0]

    def poll(self):
        "Removes first puzzle in queue"

        return self.queue.pop(0)

    def remove(self, puzzlenode):
        "Removes puzzle from queue"

        self.queue.remove(puzzlenode)

    def size(self):
        "Returns size of queue"

        return len(self.queue)

    def to_array(self):
        "Converts queue to array"

        return self.queue.copy()

    def is_empty(self):
        "Returns true if queue is empty"

        return len(self.queue) == 0
