text = open('Day20/input.txt').read().split('\n\n')

tiles = {}
for t in text:
    toks = t.split(':\n')
    key = toks[0].split(' ')[1]
    vals = toks[1].replace('\n','')
    array = []
    for y in range(0, 10):
        buf = []
        for x in range(0, 10):
            buf.append(vals[y*10+x])
        array.append(buf)
    tiles[key] = array
import math
dimension = int(math.sqrt(len(tiles.items())))

finalimage = []
processedTiles = {}
allTiles = []
corners = []
sides = []
lefts = {}
rights = {}
tops = {}
bottoms = {}
candidates = []

def getBorders(k,c):
    v = (getTop(c), getRight(c), getBottom(c), getLeft(c))
    neighbours = 0
    topcandidates = bottoms[v[0]]
    if any([x.split(' ')[0] != k.split(' ')[0] for x in topcandidates]):
        neighbours += 1
    rightcandidates = lefts[v[1]]
    if any([x.split(' ')[0] != k.split(' ')[0] for x in rightcandidates]):
        neighbours += 1
    bottomcandidates = tops[v[2]]
    if any([x.split(' ')[0] != k.split(' ')[0] for x in bottomcandidates]):
        neighbours += 1
    leftcandidates = rights[v[3]]
    if any([x.split(' ')[0] != k.split(' ')[0] for x in leftcandidates]):
        neighbours += 1
    if neighbours == 2:
        corners.append((k,v))
    elif neighbours == 3:
        sides.append((k,v))
    else:
        allTiles.append((k,v))
def getDims(k,c):
    left = getLeft(c)
    if left not in lefts:
        lefts[left] = []
    lefts[left].append(k)
    right = getRight(c)
    if right not in rights:
        rights[right] = []
    rights[right].append(k)
    top = getTop(c)
    if top not in tops:
        tops[top] = []
    tops[top].append(k)
    bottom = getBottom(c)
    if bottom not in bottoms:
        bottoms[bottom] = []
    bottoms[bottom].append(k)
def getLeft(c):
    return ''.join([x[0] for x in c])
def getRight(c):
    return ''.join([x[-1] for x in c])
def getTop(c):
    return ''.join(c[0])
def getBottom(c):
    return ''.join(c[-1])

for k,v in tiles.items():
    processedTiles[k]= []
    processedTiles[k + " R"] = []
    processedTiles[k + " F"] = []
    processedTiles[k + " T"]= []
    processedTiles[k + " TR"] = []
    processedTiles[k + " TF"] = []
    processedTiles[k + " TT"]= []
    processedTiles[k + " TTR"] = []
    processedTiles[k + " TTF"] = []
    processedTiles[k + " TTT"]= []
    processedTiles[k + " TTTR"] = []
    processedTiles[k + " TTTF"] = []
    
    reversed = []
    for x in v:
        reversed.append(x[::-1])
    flipped = []
    for x in v:
        flipped = [x] + flipped
    processedTiles[k].append(v)
    getDims(k,v)
    processedTiles[k + " R"].append(reversed)
    getDims(k + " R", reversed)
    processedTiles[k + " F"].append(flipped)
    getDims(k + " F", flipped)

    transpose = list(zip(*v[::-1]))
    reversed = []
    for x in transpose:
        reversed.append(x[::-1])
    flipped = []
    for x in transpose:
        flipped = [x] + flipped
    processedTiles[k + " T"].append(transpose)
    getDims(k + " T",transpose)
    processedTiles[k + " TR"].append(reversed)
    getDims(k + " TR", reversed)
    processedTiles[k + " TF"].append(flipped)
    getDims(k + " TF", flipped)

    transpose = list(zip(*transpose[::-1]))
    reversed = []
    for x in transpose:
        reversed.append(x[::-1])
    flipped = []
    for x in transpose:
        flipped = [x] + flipped
    processedTiles[k + " TT"].append(transpose)
    getDims(k + " TT",transpose)
    processedTiles[k + " TTR"].append(reversed)
    getDims(k + " TTR", reversed)
    processedTiles[k + " TTF"].append(flipped)
    getDims(k + " TTF", flipped)

    transpose = list(zip(*transpose[::-1]))
    reversed = []
    for x in transpose:
        reversed.append(x[::-1])
    flipped = []
    for x in transpose:
        flipped = [x] + flipped
    processedTiles[k + " TTT"].append(transpose)
    getDims(k + " TTT",transpose)
    processedTiles[k + " TTTR"].append(reversed)
    getDims(k + " TTTR", reversed)
    processedTiles[k + " TTTF"].append(flipped)
    getDims(k + " TTTF", flipped)

for k,v in tiles.items():
    reversed = []
    for x in v:
        reversed.append(x[::-1])
    flipped = []
    for x in v:
        flipped = [x] + flipped
    getBorders(k,v)
    getBorders(k + " R", reversed)
    getBorders(k + " F", flipped)

    transpose = list(zip(*v[::-1]))
    reversed = []
    for x in transpose:
        reversed.append(x[::-1])
    flipped = []
    for x in transpose:
        flipped = [x] + flipped
    getBorders(k + " T",transpose)
    getBorders(k + " TR", reversed)
    getBorders(k + " TF", flipped)

    transpose = list(zip(*transpose[::-1]))
    reversed = []
    for x in transpose:
        reversed.append(x[::-1])
    flipped = []
    for x in transpose:
        flipped = [x] + flipped
    getBorders(k + " TT",transpose)
    getBorders(k + " TTR", reversed)
    getBorders(k + " TTF", flipped)

    transpose = list(zip(*transpose[::-1]))
    reversed = []
    for x in transpose:
        reversed.append(x[::-1])
    flipped = []
    for x in transpose:
        flipped = [x] + flipped
    getBorders(k + " TTT",transpose)
    getBorders(k + " TTTR", reversed)
    getBorders(k + " TTTF", flipped)

for k,v in corners:
    sparse = {}
    for x in range(0,dimension):
        for y in range(0,dimension):
            if x == 0 and y == 0:
                sparse[(0,0)] = (k,v)
            else:
                sparse[(x,y)] = None
    candidates.append(sparse)

while len(candidates) > 0:
    current = candidates[0]
    candidates = candidates[1:]
    shouldBreak = False
    full = 1
    for y in range(0,dimension):
        if shouldBreak:
            break
        for x in range(0,dimension):
            coords = (x,y)
            if coords == (0,0):
                continue
            if shouldBreak:
                break
            if current[(x,y)] is None:
                nexttiles = []
                seenTiles = [x[1][0].split(' ')[0] for x in current.items() if x[1] is not None]
                if coords[1] == 0 and coords[0] < (dimension -1):
                    #check sides left-right
                    for n in [s for s in sides if s[0].split(' ')[0] not in seenTiles]:
                        if current[(x-1,y)][1][1] == n[1][3]:
                            nexttiles.append(n)
                elif coords[1] == 0 and coords[0] == (dimension -1):
                    #check corner left-right
                    for n in [c for c in corners if c[0].split(' ')[0] not in seenTiles]:
                        if current[(x-1,y)][1][1] == n[1][3]:
                            nexttiles.append(n)
                elif coords[0] == 0 and coords[1] < (dimension -1):
                    #check side top-bottom
                    for n in [s for s in sides if s[0].split(' ')[0] not in seenTiles]:
                        if current[(x,y-1)][1][2] == n[1][0]:
                            nexttiles.append(n)
                elif coords[0] > 0 and coords[0] < (dimension -1) and coords[1] > 0 and coords[1] < (dimension -1):
                    #check alltiles left-right and top-bottom
                    for n in [a for a in allTiles if a[0].split(' ')[0] not in seenTiles]:
                        if current[(x-1,y)][1][1] == n[1][3] and current[(x,y-1)][1][2] == n[1][0]:
                            nexttiles.append(n)
                elif coords[0] == (dimension -1) and coords[1] > 0 and coords[1] < (dimension -1):
                    #check side left-right and top-bottom
                    for n in [s for s in sides if s[0].split(' ')[0] not in seenTiles]:
                        if current[(x-1,y)][1][1] == n[1][3] and current[(x,y-1)][1][2] == n[1][0]:
                            nexttiles.append(n)
                elif coords[0] == 0 and coords[1] == (dimension -1):
                    #check corners top-bottom
                    for n in [c for c in corners if c[0].split(' ')[0] not in seenTiles]:
                        if current[(x,y-1)][1][2] == n[1][0]:
                            nexttiles.append(n)
                elif coords[0] > 0 and coords[1] == (dimension -1) and coords[0] < (dimension -1):
                    #check sides left-right and top-bottom
                    for n in [s for s in sides if s[0].split(' ')[0] not in seenTiles]:
                        if current[(x-1,y)][1][1] == n[1][3] and current[(x,y-1)][1][2] == n[1][0]:
                            nexttiles.append(n)
                elif coords[0] == (dimension -1) and coords[1] == (dimension -1):
                    #check corners left-right and top-bottom
                    for n in [c for c in corners if c[0].split(' ')[0] not in seenTiles]:
                        if current[(x-1,y)][1][1] == n[1][3] and current[(x,y-1)][1][2] == n[1][0]:
                            nexttiles.append(n)
                
                shouldBreak = True
                if len(nexttiles) > 0:
                    shouldBreak = True
                    for nt in nexttiles:
                        ccopy = dict(current)
                        ccopy[coords] = nt
                        candidates = [ccopy] + candidates
                else:
                    shouldBreak = True
            else:
                full += 1
                if full == dimension*dimension:
                    for y in range(0, dimension):
                        for linenum in range(1, 9):
                            line = []
                            for x in range(0,dimension):
                                line = line + [x for x in processedTiles[current[(x,y)][0]][0][linenum][1:-1]]
                            finalimage.append(line)

                    candidates = []

seamonsterpattern = '''                  # 
#    ##    ##    ###
 #  #  #  #  #  #   '''.split('\n')

smbuf = []
for line in seamonsterpattern:
    innerbuf = []
    for c in line:
        innerbuf.append(c)
    smbuf.append(innerbuf)
seamonsterpattern = smbuf

candidateimages = [finalimage]
reversed = []
for x in finalimage:
    reversed.append(x[::-1])
flipped = []
for x in finalimage:
    flipped = [x] + flipped
candidateimages.append(reversed)
candidateimages.append(flipped)

transpose = list(zip(*finalimage[::-1]))
reversed = []
for x in transpose:
    reversed.append(x[::-1])
flipped = []
for x in transpose:
    flipped = [x] + flipped
candidateimages.append(transpose)
candidateimages.append(reversed)
candidateimages.append(flipped)


transpose = list(zip(*transpose[::-1]))
reversed = []
for x in transpose:
    reversed.append(x[::-1])
flipped = []
for x in transpose:
    flipped = [x] + flipped
candidateimages.append(transpose)
candidateimages.append(reversed)
candidateimages.append(flipped)

transpose = list(zip(*transpose[::-1]))
reversed = []
for x in transpose:
    reversed.append(x[::-1])
flipped = []
for x in transpose:
    flipped = [x] + flipped
candidateimages.append(transpose)
candidateimages.append(reversed)
candidateimages.append(flipped)
import pyperclip
for fi in candidateimages:
    pyperclip.copy('\n'.join([''.join(y) for y in fi]))
    monstersFound = 0
    for y in range(0, 1+len(fi)-len(seamonsterpattern)):
        for x in range(0, 1+len(fi[0])-len(seamonsterpattern[0])):
            mismatch = False
            for y_ in range(0, len(seamonsterpattern)):
                if mismatch:
                    break
                for x_ in range(0, len(seamonsterpattern[0])):
                    if mismatch:
                        break
                    if seamonsterpattern[y_][x_] == '#' and fi[y+y_][x+x_] != '#':
                        mismatch = True
            if not mismatch:
                monstersFound += 1           
    if monstersFound > 0:
        roughness = 0
        for y in range(0,len(fi)):
            for x in range(0, len(fi[0])):
                if fi[y][x] == '#':
                    roughness += 1
        print(roughness-(monstersFound*15))
        candidateimages = []