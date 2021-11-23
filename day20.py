from aocutils import get_raw
from collections import defaultdict
import re

TOP, LEFT, RIGHT, BOTTOM = range(4)

get_border = [
    lambda tile: tile[0],
    lambda tile: ''.join([line[0] for line in reversed(tile)]),
    lambda tile: ''.join([line[-1] for line in tile]),
    lambda tile: tile[-1][::-1],
    lambda tile: tile[0][::-1],
    lambda tile: ''.join([line[0] for line in tile]),
    lambda tile: ''.join([line[-1] for line in reversed(tile)]),
    lambda tile: tile[-1],
]

def problem1():
    completed, tiles_by_border = assemble_image()
    corners = [completed[0][0], completed[0][-1], completed[-1][0], completed[-1][-1]]
    total = 1
    for corner in corners:
        border1 = get_border[TOP](corner)
        border2 = get_border[BOTTOM](corner)
        total *= (set(tiles_by_border[border1]) & set(tiles_by_border[border2])).pop()
    return total

def problem2():
    completed, _ = assemble_image()
    final = []
    for row in range(len(completed)):
        for line in range(1, len(completed[0][0]) - 1):
            final_row = ''
            for col in range(len(completed[0])):
                final_row += completed[row][col][line][1:-1]
            final.append(final_row)
    size = len(final[0])
    pattern = re.compile(f'(?=(#.{{{size - 19}}}#....##....##....###.{{{size - 19}}}#..#..#..#..#..#))')
    for i in range(8):
        if i % 2:
            final = rotate(flip(final, TOP))
        else:
            final = flip(final, TOP)
        string = ''.join(final)
        matches = [match for match in pattern.finditer(string)]
        if len(matches) > 0:
            ind = {0} | {size - 19 + i for i in [1, 6, 7, 12, 13, 18, 19, 20]} | {2 * size - 18 + i for i in range(1, 17, 3)}
            for match in matches:
                start, end = match.start(1), match.end(1)
                string = string[:start] + ''.join(['O' if i in ind else string[start + i] for i in range(end - start)]) + string[end:]
            return sum([1 for char in string if char == '#'])

def assemble_image():

    def get_neighbors(direction, tile_id, tile):
        border_to_match = get_border[direction](tile)[::-1]
        tile_ids = tiles_by_border[get_border[direction](tile)]
        if len(tile_ids) == 1:
            return []
        neighbor_id = tile_ids[0] if tile_ids[1] == tile_id else tile_ids[1]
        neighbor = tiles[neighbor_id]
        for i in range(8):
            if i % 2:
                neighbor = rotate(flip(neighbor, direction))
            else:
                neighbor = flip(neighbor, direction)
            if get_border[3 - direction](neighbor) == border_to_match:
                break
        if direction in [LEFT, RIGHT]:
            row = get_neighbors(direction, neighbor_id, neighbor)
            if direction == LEFT:
                return row + [neighbor]
            else:
                return [neighbor] + row
        else:
            rows = get_neighbors(direction, neighbor_id, neighbor)
            new_row = get_neighbors(LEFT, neighbor_id, neighbor) + [neighbor] + get_neighbors(RIGHT, neighbor_id, neighbor)
            if direction == TOP:
                return rows + [new_row]
            else:
                return [new_row] + rows

    tiles = [tile.split('\n') for tile in get_raw(20).split('\n\n')]
    first_id = int(tiles[0][0][5:9])
    tiles = {int(tile[0][5:9]): tile[1:] for tile in tiles}
    tiles_by_border = defaultdict(list)
    for tile_id, tile in tiles.items():
        for i in range(8):
            tiles_by_border[get_border[i](tile)].append(tile_id)
    first_tile = tiles[first_id]
    row = get_neighbors(LEFT, first_id, first_tile) + [first_tile] + get_neighbors(RIGHT, first_id, first_tile)
    completed = get_neighbors(TOP, first_id, first_tile) + [row] + get_neighbors(BOTTOM, first_id, first_tile)
    return completed, tiles_by_border

def rotate(tile):
    return [''.join(row) for row in zip(*reversed([[char for char in line] for line in tile]))]

def flip(tile, direction):
    if direction in [LEFT, RIGHT]:
        return list(reversed(tile))
    else:
        return [line[::-1] for line in tile]