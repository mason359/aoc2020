from aocutils import get_nums

def problem1():
    nums = get_nums(1)
    for x in nums:
        for y in nums:
            if x + y == 2020:
                return x * y

def problem2():
    nums = get_nums(1)
    for x in nums:
        for y in nums:
            for z in nums:
                if x + y + z == 2020:
                    return x * y * z