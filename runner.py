#!/usr/bin/env python

import sys, time

def run_problem(d, p):
    day = __import__(f'day{d}')
    problem = day.problem1 if p == 1 else day.problem2
    start = time.time()
    result = problem()
    end = time.time()
    print(f'Day {d}, Problem {p}:')
    print(f'Result: {result}')
    print(f'Finished in {end - start:0.6f}s\n')
    return end - start

def run_all():
    total_time = 0
    errors = 0
    for d in range(1, 26):
        for p in range(1, 3):
            try:
                run_time = run_problem(d, p)
                total_time += run_time
            except Exception as e:
                print(f'Day {d}, Problem {p} errored:')
                print(f'{e}\n')
                errors += 1
    if errors:
        print(f'\n {errors} errors occurred! Runtime not evaluated.')
    else:
        print(f'All days successful! Total runtime: {total_time}s')

if __name__ == "__main__":
    if sys.argv[1] == 'all':
        run_all()
    else:
        run_problem(int(sys.argv[1]), int(sys.argv[2]))
