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

contained = 0
candidates = ['shiny gold']
while len(candidates) > 0:
    top = candidates.pop()
    containedBags = containerRules[top]
    for rule in containedBags:
        for x in range(0, rule[0]):
            candidates.append(rule[1])
            contained += 1

print(contained)