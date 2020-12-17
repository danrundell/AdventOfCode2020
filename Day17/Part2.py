text = open('Day17/input.txt').readlines()
grid = {}
for y in range(0,len(text[0].replace('\n',''))):
    for x in range(0,len(text[y].replace('\n',''))):
        grid[(x,y,0,0)] = text[y][x]

for x in range(0,6):
    newgrid = {}
    candidates = list(grid.items())
    for k,v in candidates:
        for x in range(k[0]-1,k[0]+2):
            for y in range(k[1]-1,k[1]+2):
                for z in range(k[2]-1,k[2]+2):
                    for w in range(k[3]-1,k[3]+2):
                        if (x,y,z,w) not in grid:
                            grid[(x,y,z,w)] = '.'
                            continue
    candidates = list(grid.items())
    for k,v in candidates:
        active = 0
        shouldBreak = False
        for x in range(k[0]-1,k[0]+2):
            if shouldBreak:
                break
            for y in range(k[1]-1,k[1]+2):
                if shouldBreak:
                    break
                for z in range(k[2]-1,k[2]+2):
                    if shouldBreak:
                        break
                    for w in range(k[3]-1,k[3]+2):
                        if shouldBreak:
                            break
                        if k == (x,y,z,w):
                            continue
                        if (x,y,z,w) not in grid:
                            continue
                        if grid[(x,y,z,w)] == '#':
                            active += 1
                        if active > 3:
                            shouldBreak = True
        if active in [2,3] and grid[k] == '#':
            newgrid[k] = '#'
        elif active == 3:
            newgrid[k] = '#'
        else:
            newgrid[k] = '.'
    grid = newgrid
active = 0
for x in grid.values():
    if x == '#':
        active += 1
print(active)
