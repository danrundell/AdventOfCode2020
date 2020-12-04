lines = open('Day4/input.txt').read().split('\n\n')
valid_count = 0

for line in lines:
    line_ = line.replace('\n', ' ').split()
    valid = True
    for attribute in ['byr','iyr','eyr','hgt','hcl','ecl','pid']:
        if f'{attribute}:' not in line:
            valid = False
    for line__ in line_:
        attribute = line__.split(':')[0]
        value = line__.split(':')[1]
        if attribute == 'byr' and (int(value) < 1920 or int(value) > 2002):
            valid = False
        elif attribute == 'iyr' and (int(value) < 2010 or int(value) > 2020):
            valid = False
        elif attribute == 'eyr' and (int(value) < 2020 or int(value) > 2030):
            valid = False
        elif attribute == 'hgt':
            if 'in' in value:
                value = int(value.replace('in',''))
                if value < 59 or value > 76:
                    valid = False
            elif 'cm' in value:
                value = int(value.replace('cm',''))
                if value < 150 or value > 193:
                    valid = False
            else:
                valid = False
        elif attribute == 'hcl':
            if value[0] != '#':
                valid = False
            if len(value) != 7:
                valid = False
            else:
                for x in range(1,7):
                    if value[x] not in 'abcdef1234567890':
                        valid = False
        elif attribute == 'ecl':
            if value not in ['amb','blu','brn','gry','grn','hzl','oth']:
                valid = False
        elif attribute == 'pid':
            if len(value) != 9:
                valid = False
            else:
                for x in range(0,9):
                    if value[x] not in "0123456789":
                        valid = False
    if valid:
        valid_count += 1

print(valid_count)

