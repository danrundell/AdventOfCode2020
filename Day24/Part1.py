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

black = 0
for x in tiles.values():
    if x:
        black += 1
print(black)
