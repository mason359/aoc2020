from aocutils import get_nums

def problem1():
    adapters = [0] + sorted(get_nums(10))
    adapters.append(adapters[-1] + 3)
    diffs = [i[1] - i[0] for i in zip(adapters[:-1], adapters[1:])]
    ones, threes = 0, 0
    for diff in diffs:
        if diff == 1: ones += 1
        elif diff == 3: threes += 1
    return ones * threes

def problem2():
    combos = {0: 1, 1: 1, 2: 2, 3: 4, 4: 7}
    adapters = [0] + sorted(get_nums(10))
    adapters.append(adapters[-1] + 3)
    diffs = [i[1] - i[0] for i in zip(adapters[:-1], adapters[1:])]
    i = 0
    total = 1
    while i < len(diffs):
        ones = 0
        while diffs[i] == 1:
            ones += 1
            i += 1
        total *= combos[ones]
        i += 1
    return total
