text = [int(x) for x in open('Day15/input.txt').read().split(',')]

spoken = {}

turn = 1
last = 0
for x in text:
    spoken[x] = [turn]
    turn += 1
    last = x
while turn <= 2020:
    if last in spoken and len(spoken[last]) == 1:
        if 0 not in spoken:
            spoken[0] = []
        spoken[0].append(turn)
        last = 0
    elif last not in spoken:
        pass
    else:
        diff = spoken[last][-1]-spoken[last][-2]
        if diff not in spoken:
            spoken[diff] = []
        spoken[diff].append(turn)
        last = diff
    turn += 1
print(last)