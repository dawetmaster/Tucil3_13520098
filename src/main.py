import puzzle

if __name__ == "__main__":
    print("This is a module for Puzzle")
    pz = puzzle.Puzzle()
    print(pz.to_string())
    print(pz.get_heuristic_cost())
    pz.print()
    pz.move_up()
    pz.print()
    print(pz.count_all_smaller(number=16))
    print(pz.get_heuristic_cost())
    print(pz.get_tile_16_heuristic_cost())
