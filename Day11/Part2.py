text = open('Day11/input.txt').read()
grid = {}
x = 0
y = 0
for c in text:
    if c != '\n':
        grid[(x,y)] = c
        x += 1
    else:
        x = 0
        y += 1
recent = ''.join([''.join(x) for x in grid.values()])
while(True):
    nextgrid = {}
    for k,v in grid.items():
        vectors = [(0,1),(1,0),(1,1),(0,-1),(-1,0),(-1,-1),(1,-1),(-1,1)]
        count = 0
        for vec in vectors:
            kvec = (k[0]+vec[0],k[1]+vec[1])
            while(True):
                if kvec not in grid:
                    break
                if grid[kvec] == '.':
                    kvec = (kvec[0]+vec[0],kvec[1]+vec[1])
                elif grid[kvec] == '#':
                    count += 1
                    break
                elif grid[kvec] == 'L':
                    break
        if v == '#' and count >= 5:
            nextgrid[k] = 'L'
        elif v == 'L' and count == 0:
            nextgrid[k] = '#'
        else:
            nextgrid[k] = v
    grid = nextgrid
    nextrecent = ''.join([''.join(x) for x in grid.values()])
    if nextrecent == recent:
        break
    recent = nextrecent
count = 0
for v in grid.values():
    if v == '#':
        count += 1
print(count)