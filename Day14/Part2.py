text = open('Day14/input.txt').readlines()
mem = {}
currentMask = []
for line in text:
    toks = line.split(' = ')
    if toks[0] == 'mask':
        currentMask = toks[1].replace('\n','')
    else:
        address = int(toks[0].replace('mem[','').replace(']',''))
        address = f"{address:b}".format(37)
        targetValue = int(toks[1])
        while len(address) < len(currentMask):
            address = '0' + address
        targetAddresses = [address]
        for x in range(0,len(currentMask)):
            newAddresses = []
            while len(targetAddresses) > 0:
                target = targetAddresses.pop()
                if currentMask[x] == '1':
                    target = target[:x] + '1' + target[x+1:]
                    newAddresses.append(target)
                elif currentMask[x]=='X':
                    target2 = f'{target}'
                    target = target[:x] + '1' + target[x+1:]
                    target2 = target2[:x] + '0' + target2[x+1:]
                    newAddresses.append(target)
                    newAddresses.append(target2)
                else:
                    newAddresses.append(target)
            targetAddresses = newAddresses
        for targetAddress in targetAddresses:
            mem[int(targetAddress, 2)]= targetValue
        
print(sum(mem.values()))
