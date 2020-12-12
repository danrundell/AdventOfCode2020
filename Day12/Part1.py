text = open('Day12/input.txt').readlines()
pos = (0,0)
direction = 'e'
for instruction in text:
    char = instruction[0].lower()
    vect = int(instruction[1:])
    if char == 'r':
        while vect > 0:
            if direction == 'n':
                direction = 'e'
            elif direction == 'e':
                direction = 's'
            elif direction == 's':
                direction = 'w'
            elif direction == 'w':
                direction = 'n'
            vect -= 90
    elif char == 'l':
        while vect > 0:
            if direction == 'n':
                direction = 'w'
            elif direction == 'w':
                direction = 's'
            elif direction == 's':
                direction = 'e'
            elif direction == 'e':
                direction = 'n'
            vect -= 90
    else:
        if char == 'f':
            char = direction
        if char == 'n':
            pos = (pos[0],pos[1]+vect)
        if char == 'e':
            pos = (pos[0]+vect,pos[1])
        if char == 's':
            pos = (pos[0],pos[1]-vect)
        if char == 'w':
            pos = (pos[0]-vect,pos[1])
print(abs(pos[0])+abs(pos[1]))