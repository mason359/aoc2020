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

if __name__ == "__main__":
    run_problem(int(sys.argv[1]), int(sys.argv[2]))
