from aocutils import get_raw
import re

REQ_FIELDS = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
EYE_COLORS = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

def problem1():
    num_valid = 0
    passports = get_raw(4).split('\n\n')
    for passport in passports:
        fields = set([i[:3] for i in re.split(' |\n', passport)])
        if not REQ_FIELDS - fields:
            num_valid += 1
    return num_valid

def problem2():
    num_valid = 0
    passports = get_raw(4).split('\n\n')
    for passport in passports:
        data = {i[:3]: i[4:] for i in re.split(' |\n', passport)}
        if REQ_FIELDS - set(data.keys()): continue
        is_valid = True
        is_valid &= int(data['byr']) in range(1920, 2003)
        is_valid &= int(data['iyr']) in range(2010, 2021)
        is_valid &= int(data['eyr']) in range(2020, 2031)
        if data['hgt'][-2:] == 'cm':
            is_valid &= int(data['hgt'][:-2]) in range(150, 194)
        elif data['hgt'][-2:] == 'in':
            is_valid &= int(data['hgt'][:-2]) in range(59, 77)
        else:
            is_valid = False
        is_valid &= re.fullmatch('#[0-9a-f]{6}', data['hcl']) is not None
        is_valid &= data['ecl'] in EYE_COLORS
        is_valid &= re.fullmatch('\d{9}', data['pid']) is not None
        if is_valid:
            num_valid += 1
    return num_valid