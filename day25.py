from aocutils import get_raw

def problem1():
    card_pub, door_pub = [int(key) for key in get_raw(25).splitlines()]
    loop_size = 0
    subject_number = 7
    transform = 1
    while transform != card_pub:
        transform = (transform * subject_number) % 20201227
        loop_size += 1
    transform = 1
    subject_number = door_pub
    for i in range(loop_size):
        transform = (transform * subject_number) % 20201227
    return transform

def problem2():
    return 'Advent of Code 2020 Complete!'