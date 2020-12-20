text = open('Day19/input.txt').read().split('\n\n')
rulestext = text[0].split('\n')
codes = set(text[1].split('\n'))
rules = {}
resolved = {}
for r in rulestext:
    key = r.split(': ')[0]
    rules[key] = []
    allowed = r.split(': ')[1].split(' | ')
    for a in allowed:
        rules[key].append(a.split(' '))
        if '"' in a:
            resolved[key] = [[a.replace('"','')]]

rules['8'] = [['42'],['42','8']]
rules['11'] = [['42','31'],['42', '11', '31']]

longestcode = max([len(x) for x in codes])

unresolvedCount = 1
while unresolvedCount > 0:
    unresolvedCount = 0
    for k,v in rules.items():
        if k in resolved:
            continue
        if all([all([len(y) > longestcode for y in x]) for x in v]):
            continue
        if all([all([y in resolved for y in x]) for x in v]):
            v_arr = []
            for v_ in v:
                v__arr = [[]]
                for v__ in v_:
                    x_arr = []
                    for r in resolved[v__]:
                        for x in v__arr:
                            x_arr.append(x + r)
                    v__arr = x_arr
                for n in v__arr:
                    v_arr.append(n)
            resolved[k] = v_arr
        elif k == '8' and '42' in resolved:
            pass
        elif k == '11' and '42' in resolved and '31' in resolved:
            pass
        elif k == '0':
            pass
        else:
            unresolvedCount += 1

#length always 8
c42 = set([''.join(x) for x in resolved['42']])
#length always 8
c31 = set([''.join(x) for x in resolved['31']])

def matches_8(c):
    for x in range(0, len(c), 8):
        if c[x:x+8] not in c42:
            return False
    return True

def matches_11(c):
    if (len(c)/8)%2 != 0:
        return False
    firstHalf = c[0:len(c)//2]
    secondHalf = c[len(c)//2:]
    for x in range(0, len(c)//2, 8):
        if firstHalf[x:x+8] not in c42:
            return False
        if secondHalf[x:x+8] not in c31:
            return False
    return True

matches = 0

for c in codes:
    for x in range(8, len(c)-8, 8):
        if matches_8(c[0:x]) and matches_11(c[x:]):
            matches += 1
            continue 

print(matches)