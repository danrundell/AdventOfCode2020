lines = open('Day6/input.txt').read().split('\n\n')
total_count = 0
for line in lines:
    answers = [set(x) for x in line.split('\n')]
    total_count += len(set.intersection(*answers))

print(total_count)