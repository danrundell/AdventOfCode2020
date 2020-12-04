lines = open('Day4/input.txt').read().split('\n\n')
valid_count = 0
for line in lines:
    valid = True
    for attribute in ['byr','iyr','eyr','hgt','hcl','ecl','pid']:
        if f'{attribute}:' not in line:
            valid = False
    if valid:
        valid_count += 1

print(valid_count)

