from aocutils import get_lines

def problem1():
    lines = get_lines(8)
    acc = 0
    pc = 0
    executed = set()
    while pc not in executed:
        inst, val = lines[pc].split(' ')
        executed.add(pc)
        if inst == 'acc':
            acc += int(val)
            pc += 1
        elif inst == 'jmp':
            pc += int(val)
        else:
            pc += 1
    return acc

def problem2():
    lines = get_lines(8)
    acc = 0
    pc = 0
    executed = set()
    while pc != len(lines) and pc not in executed:
        inst, val = lines[pc].split(' ')
        executed.add(pc)
        if inst == 'acc':
            acc += int(val)
            pc += 1
        else:
            new_acc = does_terminate(lines, pc + int(val) if inst == 'nop' else pc + 1, executed)
            if new_acc is not None:
                return acc + new_acc
            else:
                pc += int(val) if inst == 'jmp' else 1
    print('failed')

def does_terminate(lines, pc, illegal):
    executed = set()
    acc = 0
    while pc not in (executed | illegal) and pc != len(lines):
        inst, val = lines[pc].split(' ')
        executed.add(pc)
        if inst == 'acc':
            pc += 1
            acc += int(val)
        elif inst == 'jmp':
            pc += int(val)
        else:
            pc += 1
    if pc in (executed | illegal):
        return None
    else:
        return acc
        