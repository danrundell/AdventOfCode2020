lines = open('Day5/input.txt').readlines()

seatsFound = {}
for thing in lines:
    row = [0,127]
    col = [0,7]
    for x in thing:
        if x in ['B']:
            row[0] = 1+(int((row[0]+row[1])/2))
        if x in ['F']:
            row[1] = int((row[0]+row[1])/2)
        if x in ['R']:
            col[0] = 1+(int((col[0]+col[1])/2))
        if x in ['L']:
            col[1] = int((col[0]+col[1])/2)
    if row[0] not in seatsFound:
        seatsFound[row[0]] = []
    seatsFound[row[0]].append(col[1])
    
for x in range(1,127):
    for y in range(0,8):
        if x not in seatsFound:
            continue
        if y not in seatsFound[x] and y-1 in seatsFound[x] and y+1 in seatsFound[x]:
            print(x*8+y)