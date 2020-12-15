text = open('Day14/input.txt').readlines()
mem = {}
currentMask = []
for line in text:
    toks = line.split(' = ')
    if toks[0] == 'mask':
        currentMask = toks[1].replace('\n','')
    else:
        address = int(toks[0].replace('mem[','').replace(']',''))
        targetValue = f"{int(toks[1]):b}".format(37)
        while len(targetValue) < len(currentMask):
            targetValue = '0' + targetValue
        newVal = ''
        for x in range(0,len(currentMask)):
            if currentMask[x] != 'X':
                newVal += currentMask[x]
            else:
                newVal += targetValue[x]
        mem[address]= int(newVal, 2)
print(sum(mem.values()))
