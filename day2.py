from aocutils import get_lines

def problem1():
    valid = 0
    for line in get_lines(2):
        policy, password = line.split(':')
        range_, letter = policy.split(' ')
        lower, upper = [int(i) for i in range_.split('-')]
        num = len([i for i in password if i == letter])
        if num in range(lower, upper + 1):
            valid += 1
    return valid

def problem2():
    valid = 0
    for line in get_lines(2):
        policy, password = line.split(':')
        password = password.strip()
        range_, letter = policy.split(' ')
        lower, upper = [int(i) - 1 for i in range_.split('-')]
        if (password[lower] == letter) ^ (password[upper] == letter):
            valid += 1
    return valid