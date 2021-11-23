from aocutils import get_raw

def problem1():
    fields, _, nearby = get_raw(16).split('\n\n')
    fields = [range(int(span.split('-')[0]), int(span.split('-')[1]) + 1) for field in fields.split('\n') for span in field.split(': ')[1].split(' or ')]
    nearby = [int(num) for ticket in nearby.split('\n')[1:] for num in ticket.split(',')]
    total = 0
    for num in nearby:
        if not any([num in field for field in fields]):
            total += num
    return total

def problem2():
    notes, mine, nearby = get_raw(16).split('\n\n')
    mine = [int(num) for num in mine.split('\n')[1].split(',')]
    fieldnames = [field.split(': ')[0] for field in notes.split('\n')]
    ranges = [[range(int(span.split('-')[0]), int(span.split('-')[1]) + 1) for span in field.split(': ')[1].split(' or ')] for field in notes.split('\n') ]
    nearby = list(zip(*[[int(num) for num in ticket.split(',')] for ticket in nearby.split('\n')[1:] if all([any([any([int(num) in span for span in spans]) for spans in ranges]) for num in ticket.split(',')])]))
    fields = {fieldnames[i]: ranges[i] for i in range(len(fieldnames))}
    field_locations = []
    for c, column in enumerate(nearby):
        possible = set(fieldnames)
        r = 0
        while len(possible) > 1 and r < len(column):
            possible &= {fieldname for fieldname in fieldnames if any([column[r] in span for span in fields[fieldname]])}
            r += 1
        field_locations.append(possible)
    unknown = len(field_locations)
    correct_fields = [None] * len(field_locations)
    confirmed = set()
    while unknown > 0:
        last_confirmed = confirmed
        confirmed = set()
        for i, possible in enumerate(field_locations):
            possible.difference_update(last_confirmed)
            if len(possible) == 1:
                correct_fields[i] = possible.pop()
                confirmed.add(correct_fields[i])
                unknown -= 1
    answer = 1
    for i in range(len(mine)):
        if correct_fields[i].startswith('departure'):
            answer *= mine[i]
    return answer