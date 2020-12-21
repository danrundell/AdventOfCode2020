text = open('Day21/input.txt').readlines()

allergens = set()
for x in text:
    toks = x.replace('\n','').split(' (contains ')
    if len(toks) == 0:
        continue
    alls = toks[1].replace(')','')
    for all in alls.split(', '):
        allergens.add(all)

ingredients = set()
for x in text:
    toks = x.replace('\n','').split(' (contains ')
    ings = toks[0].split(' ')
    for i in ings:
        ingredients.add(i)

possibilities = {}

for x in text:
    toks = x.replace('\n','').split(' (contains ')
    if len(toks) == 0:
        continue
    alls = toks[1].replace(')','').split(', ')
    ings = toks[0].split(' ')
    for a in alls:
        if a not in possibilities:
            possibilities[a] = set(ings)
        else:
            possibilities[a] = possibilities[a] & set(ings)

assignedings = set()
for k,v in possibilities.items():
    for x in v:
        assignedings.add(x)
count = 0
for x in text:
    toks = x.replace('\n','').split(' (contains ')    
    ings = toks[0].split(' ')
    for i in ings:
        if i not in assignedings:
            count += 1
print(count)


for k,v in possibilities.items():
    if len(v) == 1:
        for k_,v_ in possibilities.items():
            if k_ != k:
                if list(v)[0] in v_:
                    v_.remove(list(v)[0])
                    possibilities[k_] = v_
for k,v in possibilities.items():
    if len(v) == 1:
        for k_,v_ in possibilities.items():
            if k_ != k:
                if list(v)[0] in v_:
                    v_.remove(list(v)[0])
                    possibilities[k_] = v_
for k,v in possibilities.items():
    if len(v) == 1:
        for k_,v_ in possibilities.items():
            if k_ != k:
                if list(v)[0] in v_:
                    v_.remove(list(v)[0])
                    possibilities[k_] = v_
for k,v in possibilities.items():
    if len(v) == 1:
        for k_,v_ in possibilities.items():
            if k_ != k:
                if list(v)[0] in v_:
                    v_.remove(list(v)[0])
                    possibilities[k_] = v_
print('')

buf = []
for k in sorted(possibilities.keys()):
    buf.append(list(possibilities[k])[0])
print(','.join(buf))