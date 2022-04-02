import numpy as np
import puzzle

if __name__ == "__main__":
    print("This is a module for Puzzle")
    pz = puzzle.Puzzle()
    print(pz.to_string())
    print(pz.get_solvable_estimate())
    pz.print()
    pz.move_up()
    pz.print()
    print(pz.count_all_smaller())
    print(pz.get_solvable_estimate())
    print(pz.tile_16_estimate())
    arr = np.array([1, 3, 7, 5, 2, 8, 6, 9, 4, 0])
    print(arr.tolist().index(0))
