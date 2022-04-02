def compare(pznode1, pznode2):
    "Compares two puzzles"

    if pznode1.puzzle.get_total_cost() < pznode2.puzzle.get_total_cost():
        return -1
    elif pznode1.puzzle.get_total_cost() > pznode2.puzzle.get_total_cost():
        return 1
    else:
        return 0
