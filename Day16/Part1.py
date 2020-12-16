text = open('Day16/input.txt').read().split('\n\n')

rulestexts = text[0].split('\n')
yours = text[1].split('\n')[1]
theirs = [x.split(',') for x in text[2].split('\n')[1:]]

rules = []
for rulestext in rulestexts:
    toks = rulestext.split(": ")[1]
    rules.append([(int(x.split('-')[0]),int(x.split('-')[1])) for x in toks.split(' or ')])

invalids = []
for their in theirs:
    for val in their:
        valid = False
        for rule in rules:
            for subRule in rule:
                if int(val) >= subRule[0] and int(val) <= subRule[1]:
                    valid = True
        if not valid:
            invalids.append(int(val))

print(sum(invalids))