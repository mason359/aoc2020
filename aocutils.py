def get_nums(day):
    with open(f'input/input{day}.txt') as fh:
        nums = [int(line) for line in fh.readlines()]
    return nums

def get_lines(day):
    with open(f'input/input{day}.txt') as fh:
        return fh.readlines()

def get_raw(day):
    with open(f'input/input{day}.txt') as fh:
        return fh.read()