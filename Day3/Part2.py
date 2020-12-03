lines = open('Day3/input.txt').readlines()
width = len(lines[0].replace('\n',''))
pos = (0,0)
treesHit_a = 0
while (True):
    if pos[1] >= len(lines):
        break
    if lines[pos[1]][pos[0] % width] == '#':
        treesHit_a += 1
    pos = (pos[0]+1,pos[1]+1)
pos = (0,0)
treesHit_b = 0
while (True):
    if pos[1] >= len(lines):
        break
    if lines[pos[1]][pos[0] % width] == '#':
        treesHit_b += 1
    pos = (pos[0]+3,pos[1]+1)
pos = (0,0)
treesHit_c = 0
while (True):
    if pos[1] >= len(lines):
        break
    if lines[pos[1]][pos[0] % width] == '#':
        treesHit_c += 1
    pos = (pos[0]+5,pos[1]+1)
pos = (0,0)
treesHit_d = 0
while (True):
    if pos[1] >= len(lines):
        break
    if lines[pos[1]][pos[0] % width] == '#':
        treesHit_d += 1
    pos = (pos[0]+7,pos[1]+1)
pos = (0,0)
treesHit_e = 0
while (True):
    if pos[1] >= len(lines):
        break
    if lines[pos[1]][pos[0] % width] == '#':
        treesHit_e += 1
    pos = (pos[0]+1,pos[1]+2)
print(treesHit_a*treesHit_b*treesHit_c*treesHit_d*treesHit_e)