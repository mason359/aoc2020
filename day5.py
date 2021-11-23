from aocutils import get_lines

def get_seat_id(boarding_pass):
    fb = boarding_pass[:7]
    lr = boarding_pass[7:]
    row, col = 0, 0
    for i in range(7):
        row += int(fb[i] == 'B') << (6 - i)
    for i in range(3):
        col += int(lr[i] == 'R') << (2 - i)
    return row * 8 + col

def problem1():
    highest = 0
    for boarding_pass in get_lines(5):
        if (seat_id := get_seat_id(boarding_pass)) > highest: highest = seat_id
    return highest

def problem2():
    found = [False] * 1024
    for boarding_pass in get_lines(5):
        found[get_seat_id(boarding_pass)] = True
    seats_missing = True
    for i in range(1024):
        if seats_missing and found[i]:
            seats_missing = False
        elif not seats_missing and not found[i]:
            return i