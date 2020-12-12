text = open('Day12/input.txt').readlines()
shippos = (0,0)
waypointvec = (10,1)
direction = 'e'
for instruction in text:
    char = instruction[0].lower()
    vect = int(instruction[1:])
    if char == 'r':
        while vect > 0:
            if waypointvec[0] >= 0 and waypointvec[1] >= 0:
                waypointvec = (waypointvec[1],-1*waypointvec[0])
            elif waypointvec[0] >= 0 and waypointvec[1] < 0:
                waypointvec = (waypointvec[1],-1*waypointvec[0])
            elif waypointvec[0] < 0 and waypointvec[1] < 0:
                waypointvec = (waypointvec[1],-1*waypointvec[0])
            elif waypointvec[0] < 0 and waypointvec[1] >= 0:
                waypointvec = (waypointvec[1],-1*waypointvec[0])
            vect -= 90
    elif char == 'l':
        while vect > 0:
            if waypointvec[0] >= 0 and waypointvec[1] >= 0:
                waypointvec = (-1*waypointvec[1],waypointvec[0])
            elif waypointvec[0] >= 0 and waypointvec[1] < 0:
                waypointvec = (-1*waypointvec[1],waypointvec[0])
            elif waypointvec[0] < 0 and waypointvec[1] < 0:
                waypointvec = (-1*waypointvec[1],waypointvec[0])
            elif waypointvec[0] < 0 and waypointvec[1] >= 0:
                waypointvec = (-1*waypointvec[1],waypointvec[0])
            vect -= 90
    else:
        if char == 'n':
            waypointvec = (waypointvec[0],waypointvec[1]+vect)
        if char == 'e':
            waypointvec = (waypointvec[0]+vect,waypointvec[1])
        if char == 's':
            waypointvec = (waypointvec[0],waypointvec[1]-vect)
        if char == 'w':
            waypointvec = (waypointvec[0]-vect,waypointvec[1])
    if char == 'f':
        for x in range(0,vect):
            shippos = (shippos[0]+waypointvec[0],shippos[1]+waypointvec[1])
print(abs(shippos[0])+abs(shippos[1]))