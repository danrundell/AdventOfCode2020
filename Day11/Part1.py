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
        neighbours = [(k[0]+1,k[1]),(k[0]-1,k[1]),(k[0],k[1]+1),(k[0],k[1]-1),(k[0]+1,k[1]+1),(k[0]-1,k[1]-1),(k[0]+1,k[1]-1),(k[0]-1,k[1]+1)]
        count = 0
        for neighbour in neighbours:
            if neighbour not in grid:
                continue
            if grid[neighbour] == '#':
                count += 1
        if v == '#' and count >= 4:
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