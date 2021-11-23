from aocutils import get_raw

def problem1():
    return simulate(count_immediate, 4)

def problem2():
    return simulate(count_visible, 5)

def simulate(count_neighbors, max_neighbors):
    seats = [[char for char in row] for row in get_raw(11).split('\n')]
    H, W = len(seats), len(seats[0])
    seats = [['.'] * (W + 2)] + [['.'] + row + ['.'] for row in seats] + [['.'] * (W + 2)]
    old_seats = None
    while seats != old_seats:
        old_seats = seats
        seats = []
        for row in range(H + 2):
            new_row = []
            for col in range(W + 2):
                if old_seats[row][col] == '.':
                    new_row.append('.')
                    continue
                neighbors = count_neighbors(old_seats, row, col, H, W)
                if old_seats[row][col] == 'L' and neighbors == 0:
                    new_row.append('#')
                elif old_seats[row][col] == '#' and neighbors >= max_neighbors:
                    new_row.append('L')
                else:
                    new_row.append(old_seats[row][col])
            seats.append(new_row)
    return sum([sum([1 for seat in row if seat == '#']) for row in seats])

def count_immediate(seats, row, col, H, W):
    checks = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    neighbors = 0
    for (r, c) in checks:
        if seats[row + r][col + c] == '#':
            neighbors += 1
    return neighbors

def count_visible(seats, row, col, H, W):
    checks = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    neighbors = 0
    for (R, C) in checks:
        r, c = R, C
        occupied = False
        while 1 <= row + r <= H and 1 <= col + c <= W and seats[row + r][col + c] == '.':
            r += R
            c += C
        if seats[row + r][col + c] == '#':
            neighbors += 1
        if neighbors >= 5: break
    return neighbors