import math
lines = [int(x) for x in open('Day10/input.txt').readlines()]
#lines = [28,33,18,42,31,14,46,20,48,47,24,23,49,45,19,38,39,11,1,32,25,35,8,17,7,9,4,2,34,10,3]
#lines = [16,10,15,5,1,11,7,19,6,12,4]
lines = [0] + sorted(lines) + [max(lines) + 3]

partitions = []
cur = 0
for x in range(1, len(lines)):
    if lines[x]-lines[x-1] == 3:
        partitions.append(lines[cur:x])
        cur = x
partitions.append(lines[cur:])
combinations = []
for partition in partitions:
    subCombo = []
    subPartitions = [[0]]
    while len(subPartitions) > 0:
        top = subPartitions[0]
        subPartitions = subPartitions[1:]
        if partition[top[-1]] == partition[-1]:
            subCombo.append(top)
        for x in range(top[-1]+1,len(partition)):
            if partition[x]-partition[top[-1]] <= 3:
                subPartitions.append(top+[x])
    combinations.append(len(subCombo))

print(math.prod(combinations))