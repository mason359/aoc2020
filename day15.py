from aocutils import get_raw

def play_game(num_turns):
    starting_nums = [int(i) for i in get_raw(15).split(',')]
    spoken = {}
    for i in range(len(starting_nums) - 1):
        spoken[starting_nums[i]] = i
    next_ = starting_nums[-1]
    for i in range(len(starting_nums) - 1, num_turns):
        last = next_
        if last in spoken:
            next_ = i - spoken[last]
        else:
            next_ = 0
        spoken[last] = i
    return last

def play_game_preallocate(num_turns):
    starting_nums = [int(i) for i in get_raw(15).split(',')]
    turns = [None] * num_turns
    for i in range(len(starting_nums) - 1):
        turns[starting_nums[i]] = i
    next_ = starting_nums[-1]
    for i in range(len(starting_nums) - 1, num_turns):
        last = next_
        if turns[last] is not None:
            next_ = i - turns[last]
        else:
            next_ = 0
        turns[last] = i
    return last

def problem1():
    return play_game(2020)

def problem2():
    return play_game(30_000_000)