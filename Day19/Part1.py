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

unresolvedCount = 1
while unresolvedCount > 0:
    unresolvedCount = 0
    for k,v in rules.items():
        if k in resolved:
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
        else:
            unresolvedCount += 1

finals = set()
for v in resolved['0']:
    finals.add(''.join(v))

print(len(codes & finals))