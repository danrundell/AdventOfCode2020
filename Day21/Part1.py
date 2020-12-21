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
