import numpy as np
import puzzle
from puzzlenode import PuzzleNode
from puzzleprioqueue import PuzzlePrioQueue

if __name__ == "__main__":
    print("This is a module for Puzzle")
    pz = puzzle.Puzzle()
    print(pz.to_string())
    print(pz.get_solvable_estimate())
    pzqueue = PuzzlePrioQueue()
    pzqueue.add(PuzzleNode(pz.clone()))
    pz.print()
    pz.move_up()
    pz.print()
    print(pz.count_all_smaller())
    print(pz.get_solvable_estimate())
    print(pz.tile_16_estimate())
    arr = np.array([1, 3, 7, 5, 2, 8, 6, 9, 4, 0])
    print(arr.tolist().index(0))
    pzqueue.add(PuzzleNode(pz.clone()))
    for pzs in pzqueue.queue:
        print(pzs.puzzle.to_string())
