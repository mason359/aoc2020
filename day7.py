from aocutils import get_raw
import re
from collections import defaultdict

def parse_input(by_container):
    lines = re.split(' bags?\.\n?', get_raw(7))[:-1]
    bags = defaultdict(set)
    for line in lines:
        if by_container:
            if line.endswith('contain no other'): continue
            container, rest = re.split(' bags contain \d ', line)
            contained = re.split(' bags?, \d ', rest)
            for bag in contained:
                bags[bag].add(container)
        else:
            if line.endswith('contain no other'):
                container = line.split(' bags ')[0]
                bags[container] = None
            else:
                container, rest = re.split(' bags contain ', line)
                contained = re.split(' bags?, ', rest)
                bags[container] = [(int(bag[0]), bag[2:]) for bag in contained]
    return bags

def problem1():
    return problem1_help('shiny gold', parse_input(True), set())

def problem1_help(color, bags, containers):
    total = 0
    for bag in bags[color]:
        if bag not in containers:
            containers.add(bag)
            total += problem1_help(bag, bags, containers) + 1
    return total

def problem2():
    return problem2_help('shiny gold', parse_input(False), 1)

def problem2_help(color, bags, factor):
    if bags[color] is None: return 0
    total = 0
    for bag in bags[color]:
        total += factor * bag[0] + problem2_help(bag[1], bags, factor * bag[0])
    return total