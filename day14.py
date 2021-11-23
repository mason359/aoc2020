from aocutils import get_raw

def problem1():
    lines = get_raw(14).splitlines()
    mem = {}
    i = 0
    while i < len(lines):
        mask = lines[i].split(' = ')[1]
        ones = int(''.join(['1' if bit == '1' else '0' for bit in mask]), 2)
        zeros = int(''.join(['0' if bit == '0' else '1' for bit in mask]), 2)
        i += 1
        while i < len(lines) and 'mem' in lines[i]:
            address, val = lines[i].split('] = ')
            index = int(address.split('[')[1])
            val = int(val)
            val |= ones
            val &= zeros
            mem[index] = val
            i += 1
    return sum(mem.values())

def problem2():
    lines = get_raw(14).splitlines()
    mem = {}
    i = 0
    while i < len(lines):
        mask = lines[i].split(' = ')[1]
        floating = []
        ones = int(''.join(['1' if bit == '1' else '0' for bit in mask]), 2)
        zeros = int(''.join(['0' if bit == 'X' else '1' for bit in mask]), 2)
        floating = [i for i in range(len(mask)) if mask[i] == 'X']
        i += 1
        while i < len(lines) and 'mem' in lines[i]:
            address, val = lines[i].split('] = ')
            index = int(address.split('[')[1])
            index |= ones
            index &= zeros
            val = int(val)
            write_to_mem(mem, index, val, floating)
            i += 1
    return sum(mem.values())

def write_to_mem(mem, index, val, floating):
    if len(floating) == 0:
        mem[index] = val
        return
    write_to_mem(mem, index, val, floating[1:])
    write_to_mem(mem, index | (1 << (35 - floating[0])), val, floating[1:])