lines = [int(x) for x in open('Day9/input.txt').readlines()]
cur = 25
shouldRun = True
while(shouldRun):
    matchFound = False
    for x in range(cur-25,cur):
        for y in range(x,cur):
            if lines[x]+lines[y] == lines[cur]:
                matchFound = True
                continue
        if matchFound:
            continue
    if not matchFound:
        print(lines[cur])
        shouldRun = False
    else:
        cur += 1