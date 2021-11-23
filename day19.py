from aocutils import get_raw
import re

def parse_input():
    rule_list, messages = get_raw(19).split('\n\n')
    rule_list = rule_list.splitlines()
    messages = messages.splitlines()
    rules = {}
    for rule in rule_list:
        rule_num, pattern = rule.split(': ')
        pattern = [part.split(' ') for part in pattern.split(' | ')]
        rules[rule_num] = pattern
    return rules, messages

def problem1():
    rules, messages = parse_input()
    pattern = re.compile(get_pattern(rules, '0', {}))
    return sum([1 for message in messages if pattern.fullmatch(message)])

def problem2():
    rules, messages = parse_input()
    cached = {}
    pattern = get_pattern(rules, '0', cached)
    rule8 = cached['8']
    rule11 = cached['11']
    rule42 = cached['42']
    rule31 = cached['31']
    pattern_check = pattern.replace(rule11, '#')
    pattern = pattern_check.replace(rule8, f'{rule8[:-1]}+)')
    total = 0
    for message in messages:
        for i in range(1, 10):
            pattern_check = pattern.replace('#', (rule42 * i) + (rule31 * i))
            if re.fullmatch(pattern_check, message) is not None:
                total += 1
                break
    return total

def get_pattern(rules, num, cached):
    if num in cached:
        return cached[num]
    if rules[num][0][0].startswith('"'):
        cached[num] = f'({rules[num][0][0][1]})'
        return cached[num]
    patterns = []
    for option in rules[num]:
        pattern = ''
        for part in option:
            pattern += get_pattern(rules, part, cached)
        patterns.append(pattern)
    cached[num] = f'({"|".join(patterns)})'
    return cached[num]