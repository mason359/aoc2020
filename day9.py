from aocutils import get_nums
from functools import reduce

def problem1():
    preamble_len = 25
    nums = get_nums(9)
    preamble = set(nums[:preamble_len])
    for i in range(preamble_len, len(nums)):
        if not reduce(lambda x, y: x or y, [nums[i] - n in preamble for n in preamble]):
            return nums[i]
        else:
            preamble.remove(nums[i - preamble_len])
            preamble.add(nums[i])

def problem2():
    target = problem1()
    nums = get_nums(9)
    start, end = 0, 1
    total = nums[start] + nums[end]
    while total != target:
        if total < target:
            end += 1
            total += nums[end]
        else:
            total -= nums[start]
            start += 1
    span = nums[start:end + 1]
    return min(span) + max(span)
