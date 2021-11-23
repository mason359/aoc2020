from aocutils import get_raw

directions = {
    'e': (1, 0),
    'w': (-1, 0),
    'ne': (1, 1),
    'nw': (0, 1),
    'se': (0, -1),
    'sw': (-1, -1)
}

def problem1():
    black = init_floor()
    return len(black)

def problem2():
    num_days = 100
    black = init_floor()
    for i in range(num_days):
        new_black = set()
        neighbors = set()
        for tile in black:
            neighbors |= set(get_neighbors(*tile))
        for tile in neighbors:
            num_neighbors = sum([1 for neighbor in get_neighbors(*tile) if neighbor in black])
            if tile in black and num_neighbors in [1, 2]:
                new_black.add(tile)
            elif tile not in black and num_neighbors == 2:
                new_black.add(tile)
        black = new_black
    return len(black)

def init_floor():
    lines = get_raw(24).splitlines()
    black = set()
    for line in lines:
        x, y = 0, 0
        i = 0
        while i < len(line):
            if line[i:i + 2] in {'ne', 'nw', 'se', 'sw'}:
                direction = line[i:i + 2]
                i += 2
            else:
                direction = line[i]
                i += 1
            x += directions[direction][0]
            y += directions[direction][1]
        if (x, y) in black:
            black.remove((x, y))
        else:
            black.add((x, y))
    return black

def get_neighbors(x, y):
    neighbors = [(-1, 0), (0, 1), (1, 1), (1, 0), (0, -1), (-1, -1)]
    for xi, yi in neighbors:
        yield (x + xi, y + yi)