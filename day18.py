from functools import reduce

from aocutils import get_raw

def problem1():
    return run(solve_sequential)

def problem2():
    return run(solve_peasmd)

def run(solve_problem):
    problems = [line.replace(' ', '') for line in get_raw(18).splitlines()]
    return sum([solve_problem(problem, 0)[0] for problem in problems])

def solve_sequential(problem, i):
    total = 0
    operator = '+'
    while i < len(problem) and problem[i] != ')':
        if problem[i] in ['+', '*']:
            operator = problem[i]
        elif problem[i] == '(':
            operand, i = solve_sequential(problem, i + 1)
            if operator == '+':
                total += operand
            else:
                total *= operand
        else:
            if operator == '+':
                total += int(problem[i])
            else:
                total *= int(problem[i])
        i += 1
    return total, i

def solve_peasmd(problem, i):
    operands = [[]]
    while i < len(problem) and problem[i] != ')':
        if problem[i] == '*':
            operands.append([])
        elif problem[i] == '+':
            pass
        elif problem[i] == '(':
            operand, i = solve_peasmd(problem, i + 1)
            operands[-1].append(int(operand))
        else:
            operands[-1].append(int(problem[i]))
        i += 1
    return reduce(lambda x, y: x * y, [sum(addition) for addition in operands]), i