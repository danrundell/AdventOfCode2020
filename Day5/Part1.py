lines = open('Day5/input.txt').readlines()

max_ = 0
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
    pass_ = row[0]*8+col[1]
    if pass_ > max_:
        max_ = pass_

print(max_)