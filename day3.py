from aocutils import get_lines

def find_trees(right, down):
    trees = 0
    row, col = down - 1, 0
    for line in get_lines(3):
        row += 1
        if row != down: continue
        if line[col] == '#': trees += 1
        col += right
        col %= len(line)
        row %= down
    return trees

def problem1():
    return find_trees(3, 1)

def problem2():
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    total = 1
    for slope in slopes:
        total *= find_trees(slope[0], slope[1])
    return total