lines = open('Day7/input.txt').readlines()

containerRules = {}
for line in lines:
    tokens = line.split(' bags contain ')
    contents = tokens[1].replace('.','').split(', ')
    parsedContents = []
    for content in contents:
        tokens__ = content.split(' ')
        if tokens__[0] == 'no':
            parsedContents.append((0,''))
        else:
            parsedContents.append((int(tokens__[0]), tokens__[1] + ' ' + tokens__[2]))
    containerRules[tokens[0]] = parsedContents

candidates = []
found = set()
for (key, value) in containerRules.items():
    if 'shiny gold' in [x[1] for x in value]:
        candidates.append(key)
        found.add(key)

while len(candidates) > 0:
    top = candidates.pop()
    for (key, value) in containerRules.items():
        if top in [x[1] for x in value]:
            candidates.append(key)
            found.add(key)

print(len(found))