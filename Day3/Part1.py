lines = open('Day3/input.txt').readlines()
width = len(lines[0].replace('\n',''))
pos = (0,0)
treesHit = 0
while (True):
    if pos[1] >= len(lines):
        break
    if lines[pos[1]][pos[0] % width] == '#':
        treesHit += 1
    pos = (pos[0]+3,pos[1]+1)
print(treesHit)