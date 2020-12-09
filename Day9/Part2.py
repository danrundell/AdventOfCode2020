lines = [int(x) for x in open('Day9/input.txt').readlines()]
cur = 0
shouldRun = True
target = 530627549
while(shouldRun):
    soFar = 0
    for x in range(cur,len(lines)):
        soFar += lines[x]
        if soFar == target:
            print(min(lines[cur:x])+max(lines[cur:x]))
            shouldRun = False
            continue
        if soFar > target:
            break
    cur += 1