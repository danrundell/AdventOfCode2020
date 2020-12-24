text = open('Day24/input.txt').readlines()
tiles = {}
for tile in text:
    tile = tile.strip()
    current = (0,0,0)
    while len(tile) > 0:
        top = tile[0]
        tile = tile[1:]
        if top == 'e':
            current = (current[0]+1,current[1]-1, current[2])
        elif top == 'w':
            current = (current[0]-1,current[1]+1, current[2])
        elif top in ['n','s']:
            top += tile[0]
            tile = tile[1:]
            if top == 'ne':
                current = (current[0]+1,current[1], current[2]-1)
            elif top == 'sw':
                current = (current[0]-1,current[1], current[2]+1)
            elif top == 'nw':
                current = (current[0],current[1]+1,current[2]-1)
            elif top == 'se':
                current = (current[0],current[1]-1,current[2]+1)
            else:
                print('invalid input detected')
        else:
            print('invalid input detected')
    if current in tiles:
        tiles[current] = not tiles[current]
    else:
        tiles[current] = True

for x in range(0,100):
    newtiles = {}
    for k,v in tiles.items():
        sixadjacent = [
            (k[0]+1,k[1]-1,k[2]),
            (k[0]-1,k[1]+1,k[2]),
            (k[0]+1,k[1],k[2]-1),
            (k[0]-1,k[1],k[2]+1),
            (k[0],k[1]+1,k[2]-1),
            (k[0],k[1]-1,k[2]+1)
            ]
        for adj in sixadjacent:
            if adj not in newtiles:
                newtiles[adj] = False
        newtiles[k] = v
    tiles = newtiles
    newtiles = {}
    for k,v in tiles.items():
        sixadjacent = [
            (k[0]+1,k[1]-1,k[2]),
            (k[0]-1,k[1]+1,k[2]),
            (k[0]+1,k[1],k[2]-1),
            (k[0]-1,k[1],k[2]+1),
            (k[0],k[1]+1,k[2]-1),
            (k[0],k[1]-1,k[2]+1)
            ]
        if v:
            neighbours = 0
            for adj in sixadjacent:
                if adj in tiles and tiles[adj]:
                    neighbours += 1
            if neighbours == 0 or neighbours > 2:
                newtiles[k] = False
            else:
                newtiles[k] = v
        else:
            neighbours = 0
            for adj in sixadjacent:
                if adj in tiles and tiles[adj]:
                    neighbours += 1
            if neighbours == 2:
                newtiles[k] = True
            else:
                newtiles[k] = v
    tiles = newtiles

total = 0
for v in tiles.values():
    if v:
        total += 1
print(total)
