from aocutils import get_lines
from collections import defaultdict

def problem1():
    instructions = [(line[0], int(line[1:])) for line in get_lines(12)]
    DIRS = ['E', 'S', 'W', 'N']
    distances = defaultdict(int)
    direction = 0
    for (inst, val) in instructions:
        if inst == 'F':
            distances[DIRS[direction]] += val
        elif inst == 'R':
            direction += val // 90
        elif inst == 'L':
            direction -= val // 90
        else:
            distances[inst] += val
        direction %= 4
    return abs(distances['N'] - distances['S']) + abs(distances['E'] - distances['W'])

def problem2():
    instructions = [(line[0], int(line[1:])) for line in get_lines(12)]
    DIRS = {'E': 0, 'S': 1, 'W': 2, 'N': 3}
    waypoint = [10, 0, 0, 1]
    ship = [0, 0, 0, 0]
    for (inst, val) in instructions:
        if inst == 'F':
            ship = [ship[i] + waypoint[i] * val for i in range(4)]
        elif inst in {'R', 'L'}:
            if inst == 'R':
                val = 360 - val
            waypoint = [waypoint[i % 4] for i in range(val // 90, val // 90 + 4)]
        else:
            waypoint[DIRS[inst]] += val
    return sum([abs(ship[i] - ship[i + 2]) for i in range(2)])