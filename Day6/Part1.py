lines = open('Day6/input.txt').read().split('\n\n')
total_count = 0
for line in lines:
    line = line.replace('\n','')
    total_count += len(set(line))

print(total_count)