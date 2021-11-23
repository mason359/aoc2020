from aocutils import get_lines

def problem1():
    [time, buses] = get_lines(13)
    time = int(time)
    buses = [int(bus) for bus in buses.split(',') if bus != 'x']
    bus = min(buses, key=lambda x: -time % x)
    return bus * (-time % bus)

def problem2():
    buses = [int(bus) if bus != 'x' else 1 for bus in get_lines(13)[1].split(',')]
    factor, increment = 1, 1
    for idx in range(1, len(buses)):
        if buses[idx] == 1: continue
        i = 0
        while (buses[0] * (factor + i * increment) + idx) % buses[idx] != 0:
            i += 1
        factor += i * increment
        increment *= buses[idx]
    return buses[0] * factor