from aocutils import get_raw

def problem1():
    return simulate(lambda x, y: (x, y, 0), get_neighbors_3d)

def problem2():
    return simulate(lambda x, y: (x, y, 0, 0), get_neighbors_4d)

def simulate(create_cube, get_neighbors):
    num_cycles = 6
    lines = get_raw(17).splitlines()
    active = set()
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == '#':
                active.add(create_cube(x, y))
    for _ in range(num_cycles):
        new_active = set()
        domain = set()
        for cube in active:
            domain |= set(get_neighbors(*cube))
        for cube in domain:
            active_neighbors = 0
            for neighbor in get_neighbors(*cube):
                if neighbor in active:
                    active_neighbors += 1
                if active_neighbors >= 4: break
            if cube in active and active_neighbors in [2, 3]:
                new_active.add(cube)
            elif cube not in active and active_neighbors == 3:
                new_active.add(cube)
        active = new_active
    return len(active)

def get_neighbors_3d(x, y, z):
    for ix in range(-1, 2):
        for iy in range(-1, 2):
            for iz in range(-1, 2):
                if (ix, iy, iz) == (0, 0, 0): continue
                yield (x + ix, y + iy, z + iz)

def get_neighbors_4d(x, y, z, w):
    for ix in range(-1, 2):
        for iy in range(-1, 2):
            for iz in range(-1, 2):
                for iw in range(-1, 2):
                    if (ix, iy, iz, iw) == (0, 0, 0, 0): continue
                    yield (x + ix, y + iy, z + iz, w + iw)
        