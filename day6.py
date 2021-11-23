from aocutils import get_raw
from functools import reduce

def problem1():
    return sum([len(set([let for let in group if let != '\n'])) for group in get_raw(6).split('\n\n')])

def problem2():
    return sum([len(reduce(lambda x, y: x.intersection(y), [set([let for let in person]) for person in group.split('\n')])) for group in get_raw(6).split('\n\n')])