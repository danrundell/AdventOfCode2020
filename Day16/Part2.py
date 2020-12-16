text = open('Day16/input.txt').read().split('\n\n')
rulestexts = text[0].split('\n')
yours = [int(x) for x in text[1].split('\n')[1].split(',')]
theirs = [x.split(',') for x in text[2].split('\n')[1:]]

rules = []
for rulestext in rulestexts:
    toks = rulestext.split(": ")
    rules.append([(toks[0], int(x.split('-')[0]),int(x.split('-')[1])) for x in toks[1].split(' or ')])

invalids = []
ctr = 0
for their in theirs:
    for val in their:
        valid = False
        for rule in rules:
            for subRule in rule:
                if int(val) >= subRule[1] and int(val) <= subRule[2]:
                    valid = True
        if not valid:
            invalids.append(ctr)
    ctr += 1

valids = []
for x in range(0,len(theirs)):
    if x not in invalids:
        valids.append(theirs[x])

fields = [(x[0], [x for x in range(0,len(valids[0]))]) for x in [r[0] for r in rules]]
finals = {}
while(len(fields) > 0):
    eligible = fields.pop(0)
    eligibleFields = [x for x in eligible[1] if x not in finals]
    if len(eligible[1]) == 1:
        finals[eligible[1][0]] = eligible[0]
        continue
    for v in valids:
        for x in range(0,len(v)):
            if x not in eligibleFields:
                continue
            ticketField = int(v[x])
            rule = [r for r in rules if r[0][0] == eligible[0]][0]
            valid = False
            for r in rule:
                if r[1] <= ticketField and r[2] >= ticketField:
                    valid = True
            if not valid:
                eligibleFields = [e for e in eligibleFields if e != x]
    fields.append((eligible[0], eligibleFields))

sum = 1
for x in range(0,len(yours)):
    if 'departure' in finals[x]:
        sum *= yours[x]
print(sum)